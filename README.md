# sistema-automatizacion-whatsapp
# Sistema Automatizado de Fidelización y Envío Masivo por WhatsApp

Este proyecto consiste en un sistema de automatización desarrollado en *Python* integrado con *Microsoft Excel*. Su objetivo principal es optimizar la comunicación y fidelización de clientes mediante el envío programado y personalizado de mensajes de texto e imágenes en fechas específicas.

El sistema está diseñado para operar de forma autónoma mediante el *Programador de Tareas de Windows*, lo que permite su ejecución diaria sin intervención humana directa.

---

## ✨ Características Principales

* *Base de Datos Dinámica*: Gestión integral de clientes, categorías y agendas de envío a través de hojas de cálculo (Excel).
* *Filtro por Día de la Semana*: El script detecta automáticamente el día actual (ej. Lunes, Sábado) y procesa únicamente los contenidos planificados para esa fecha.
* *Mensajes 100% Personalizados*: Estructuración algorítmica de textos combinando nombres de clientes y variables específicas extraídas del Excel.
* *Automatización de Interfaz Gráfica (GUI)*: Simulación nativa de eventos de teclado y control del navegador Google Chrome para interactuar con WhatsApp Web.
* *Control Inteligente de Pestañas*: Sistema optimizado de cierre forzado de solapas en caliente para evitar la saturación de memoria y el solapamiento de sesiones en el servidor.
* *Alojamiento Cloud para Contenidos*: Consumo de recursos gráficos dinámicos alojados de forma externa mediante repositorios remotos.

---

## 🛠️ Tecnologías y Librerías Utilizadas

* *Python 3.11* (Motor principal de desarrollo).
* *Pandas*: Para la manipulación, lectura y filtrado estructurado de la base de datos en Excel.
* *PyWhatKit*: Librería encargada de la vinculación y puente técnico con la API e interfaz de WhatsApp Web.
* *Keyboard*: Simulación de comandos de teclado de bajo nivel (ctrl+w) para la optimización del navegador.
* *Time / Datetime*: Gestión de cronómetros, pausas de seguridad (wait_time) y análisis de fechas del sistema operativo.
* *Programador de Tareas de Windows*: Orquestador del sistema para la ejecución automatizada diaria a las 09:00 AM.

---

## 🚀 Flujo de Funcionamiento Interno

1. *Desencadenamiento*: Windows activa el entorno virtual de Python en el horario programado.
2. *Lectura y Cruce de Datos*: El script analiza el archivo Excel, detecta el día calendario y filtra la cola de envíos correspondientes.
3. *Procesamiento de Interfaz*: Se levanta una instancia de Google Chrome con una pausa de seguridad de 35 segundos para garantizar la carga completa del entorno web.
4. *Envío y Cierre*: Se dispara el mensaje personalizado con la imagen y se fuerza el cierre de la solapa mediante comandos de teclado para mantener el navegador limpio.
5. *Reporte Automático*: Se genera una bitácora detallada con marcas de tiempo en el archivo histórico del sistema.
