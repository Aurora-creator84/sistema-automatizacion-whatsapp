import os
import time
import urllib.request
import pywhatkit as kit
import webbrowser as web



def mandar_mensajes(lista_clientes, dia_actual):
    print("\n--- INICIANDO ENVÍOS AUTOMÁTICOS DESDE EL EXCEL ---")
    resultados_envio = []

    # Creamos una carpeta en tu Escritorio para guardar temporalmente las imágenes de internet
    CARPETA_TEMPORAL = r"C:\Users\Usuario\OneDrive\Escritorio\tif\temp_imagenes"
    if not os.path.exists(CARPETA_TEMPORAL):
        os.makedirs(CARPETA_TEMPORAL)

    for persona in lista_clientes:
        nombre = persona["nombre"]
        tipo = persona["tipo"]
        telefono = str(persona["telefono"]).strip().replace(" ", "")

        # Tomamos el texto y la URL que Python cruzó automáticamente desde la hoja Contenidos
        mensaje_cuerpo = persona.get("texto", "Hola! Te enviamos tu información.")
        url_imagen = persona.get("imagen_url", "")

        # Y agregá justo abajo esta línea mágica para corregir los links de GitHub:
        if "github.com" in str(url_imagen):
            if "/blob/" in str(url_imagen):
             url_imagen = str(url_imagen).replace("/blob/", "/raw/")

        # Definimos dónde se va a descargar la foto en tu computadora por unos segundos
        ruta_imagen_local = os.path.join(
            CARPETA_TEMPORAL, f"temp_{nombre.replace(' ', '_')}.jpg"
        )

        try:
            # SI LA FILA TIENE UNA URL DE IMAGEN, SE LA SUMAMOS AL TEXTO
            if url_imagen and str(url_imagen).startswith("http"):
                mensaje_final = f"{mensaje_cuerpo}\n\n📷 Ver imagen adjunta: {url_imagen}"
            else:
                mensaje_final = mensaje_cuerpo

            print(f"Abriendo chat de WhatsApp y enviando mensaje masivo a {nombre}...")
            
            # Al activar close_time=3, la librería espera a enviar el mensaje y 
            # cierra la pestaña de forma interna sin requerir que toques el teclado ni hagas clics.
            kit.sendwhatmsg_instantly(
                phone_no=f"+{telefono}",
                message=mensaje_final,
                wait_time=35,       # Le damos 35 segundos para que cargue con calma cualquier internet lento
                tab_close=False,
          
            )
              # --- TRUCO DE CONTROL DE PESTAÑAS ---
            # Le damos 5 segundos para que la librería simule el 'Enter' nativo
            time.sleep(5)
            
            # Forzamos manualmente el cierre de la solapa actual desde Python
            import keyboard
            keyboard.press_and_release('ctrl+w')
            print(f"Pestaña cerrada a la fuerza para {nombre} para evitar duplicados.")

           
            resultados_envio.append({
                "nombre": nombre, 
                "tipo": tipo, 
                "telefono": telefono, 
                "estado": "Exitoso", 
                "detalle": "Enviado por canal nativo"
            })
            
            # Pausa de seguridad limpia de 5 segundos antes de pasar al próximo cliente del Excel
            time.sleep(20)

        except Exception as e:
            print(f"❌ No se pudo enviar el mensaje a {nombre}: {e}")
            resultados_envio.append({
                "nombre": nombre, 
                "tipo": tipo, 
                "telefono": telefono, 
                "estado": "Error", 
                "detalle": str(e)
            })
    return resultados_envio
