# Flujo-Automatico-con-Prefect-para-Procesar-Archivos-CSV
 Este proyecto utiliza Prefect para automatizar el proceso de descarga, procesamiento y almacenamiento de datos de archivos CSV.

 ## Descripción 
 El flujo descarga un archivo CSV desde una URL, procesa los datos (contando el número de filas) y guarda el resultado en un archivo de texto.

 ## Evidencia

 ![Evidencia1](img/evidencia2)
 ![Evidencia2](img/evidencia1)
 ![Evidencia3](img/evidencia3)


 ## Características del Proyecto

- **Automatización de tareas con Prefect**: El flujo está diseñado para ser completamente automatizado, lo que facilita la ejecución de tareas repetitivas como la descarga de archivos, procesamiento de datos y almacenamiento de resultados.

- **Descarga de archivo CSV desde una URL**: El proyecto descarga automáticamente un archivo CSV desde una URL predefinida, lo que ahorra tiempo y evita tener que hacerlo manualmente.

- **Procesamiento de datos con Pandas**: Utiliza **pandas**, una de las librerías más poderosas para procesamiento de datos en Python, para leer el archivo CSV y calcular el número de filas.

- **Manejo de resultados**: El número de filas del archivo CSV descargado se guarda en un archivo de texto dentro de la carpeta `output/`, lo que permite almacenar y consultar los resultados fácilmente.

- **Flujo Prefect**: El proyecto está construido sobre **Prefect**, lo que permite gestionar tareas de manera eficiente, controlar dependencias entre tareas y ejecutar flujos de trabajo de forma ordenada.

- **Escalabilidad**: Aunque este es un ejemplo simple, el flujo de trabajo se puede extender fácilmente para realizar tareas más complejas, como transformar los datos, integrarse con bases de datos o incluso enviar los resultados a otros sistemas.

- **Documentación detallada**: El proyecto viene con un archivo `README.md` bien documentado que explica cómo instalar, ejecutar y contribuir al proyecto, lo que facilita su uso incluso para personas que no están familiarizadas con el flujo.

## Requisitos 

- **Python 3.7+**: Este proyecto está diseñado para ser ejecutado con Python 3.7 o versiones superiores.
- **Conexión a Internet**: Se requiere acceso a Internet para descargar el archivo CSV desde una URL externa.

### Dependencias

Este proyecto utiliza las siguientes librerías de Python que se deben instalar para su correcto funcionamiento:

- **Prefect 1.4**: Herramienta de orquestación para la automatización de flujos de trabajo.
- **pandas**: Biblioteca para la manipulación y análisis de datos.
- **requests**: Biblioteca para realizar peticiones HTTP y descargar archivos.

 ## Instalación

 1. Clona este repositorio: 
    ´´´bash
    git clone https://github.com/AlonsoCanales-Prog/Flujo-Autom-tico-con-Prefect-para-Procesar-Archivos-CSV.git
