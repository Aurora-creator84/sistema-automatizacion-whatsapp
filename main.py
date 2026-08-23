import os
import csv
from datetime import datetime
import pandas as pd
import envios  # Importa tu archivo envios.py corregido

# Configuración de rutas de archivos
RUTA_EXCEL = r"C:\Users\Usuario\OneDrive\Desktop\pet\mis_clientes.xlsx.xlsx"
ARCHIVO_LOG = r"C:\Users\Usuario\OneDrive\Escritorio\tif\historial_envios.csv"

def obtener_dia_semana_espanol():
    """Obtiene el nombre del día de la semana actual en español con la primera letra en mayúscula."""
    dias = {
        0: "Lunes",
        1: "Martes",
        2: "Miércoles",
        3: "Jueves",
        4: "Viernes",
        5: "Sábado",
        6: "Domingo"
    }
    return dias[datetime.now().weekday()]

def main():
    dia_actual = obtener_dia_semana_espanol()
    print("====================================================")
    print(f"--- INICIANDO PROCESO AUTOMÁTICO PARA EL DÍA: {dia_actual} ---")
    print("====================================================")

    # 1. Verificar si el archivo de Excel existe en la ruta
    if not os.path.exists(RUTA_EXCEL):
        print(f"❌ Error: No se encontró el archivo de Excel en la ruta: {RUTA_EXCEL}")
        return

    try:
        # 2. Leer las dos pestañas del Excel usando pandas
        print("Leyendo bases de datos de Excel...")
        df_clientes = pd.read_excel(RUTA_EXCEL, sheet_name="Clientes")
        df_contenidos = pd.read_excel(RUTA_EXCEL, sheet_name="Contenidos")

        # Limpiar espacios vacíos o diferencias de mayúsculas/minúsculas en las columnas clave
        df_clientes["tipo"] = df_clientes["tipo"].astype(str).str.strip()
        df_contenidos["dia"] = df_contenidos["dia"].astype(str).str.strip()
        df_contenidos["tipo"] = df_contenidos["tipo"].astype(str).str.strip()

        # 3. Filtrar los contenidos agendados estrictamente para el día de hoy
        print(f"Buscando contenidos planificados para hoy ({dia_actual})...")
        contenidos_hoy = df_contenidos[df_contenidos["dia"] == dia_actual]

        if contenidos_hoy.empty:
            print(f"⚠️ Aviso: No hay contenidos ni imágenes planificadas en el Excel para el día {dia_actual}.")
            return

        # 4. Cruzar los clientes con los contenidos que les corresponden según su 'tipo' (Nuevo, Frecuente, etc.)
        # Esto junta de forma automática el teléfono de la persona con su respectivo mensaje e imagen_url
        df_envios_hoy = pd.merge(df_clientes, contenidos_hoy, on="tipo", how="inner")

        # Convertir el resultado final de pandas a una lista de diccionarios para envios.py
        lista_clientes_a_enviar = df_envios_hoy.to_dict(orient="records")

        if not lista_clientes_a_enviar:
            print(" No se encontraron clientes cuyos perfiles coincidan con los contenidos de hoy.")
            return

        # 5. Ejecutar la función de envíos masivos por WhatsApp Web
        print(f"Se encontraron {len(lista_clientes_a_enviar)} envíos programados para hoy.")
        resultados = envios.mandar_mensajes(lista_clientes_a_enviar, dia_actual)

        # 6. Guardar el reporte de resultados en el archivo de historial CSV
        print("\nGuardando reporte en el historial...")
        existe_log = os.path.exists(ARCHIVO_LOG)
        columnas_log = ["nombre", "tipo", "telefono", "estado", "detalle"]

        with open(ARCHIVO_LOG, mode="a", newline="", encoding="utf-8") as archivo:
            writer = csv.DictWriter(archivo, fieldnames=columnas_log)
            
            if not existe_log:
                writer.writeheader()  # Si el archivo CSV no existe, escribe los títulos
                
            writer.writerows(resultados)

        print("====================================")
        print("=========== PROCESO TERMINADO =======")
        print(f"Log guardado en: {ARCHIVO_LOG}")
        print("====================================")

    except Exception as e:
        print(f"❌ Ocurrió un error general en el sistema: {e}")

if __name__ == "__main__":
    main()

