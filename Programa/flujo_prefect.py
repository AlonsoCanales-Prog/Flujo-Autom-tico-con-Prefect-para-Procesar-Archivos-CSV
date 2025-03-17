from prefect import task, Flow
import requests
import pandas as pd
import os

# Crear la carpeta output si no existe
if not os.path.exists("output"):
    os.makedirs("output")

# 1. Descargar archivo desde una URL
@task
def download_csv(url):
    response = requests.get(url)
    if response.status_code == 200:
        file_path = "output/data.csv"  # Guardar en la carpeta output
        with open(file_path, "wb") as f:
            f.write(response.content)
        return file_path
    else:
        raise Exception("Error al descargar el archivo")

# 2. Leer el archivo CSV
@task
def read_csv(file_path):
    return pd.read_csv(file_path)

# 3. Contar las filas en el CSV
@task
def count_rows(df):
    return len(df)

# 4. Guardar el número de filas en un archivo de texto
@task
def save_count_to_file(count):
    with open("output/row_count.txt", "w") as f:  # Guardar en la carpeta output
        f.write(f"Número de filas: {count}")

# Definir el flujo
with Flow("CSV-Processing-Flow") as flow:
    url = "https://people.sc.fsu.edu/~jburkardt/data/csv/addresses.csv"  # URL de ejemplo
    file_path = download_csv(url)
    df = read_csv(file_path)
    row_count = count_rows(df)
    save_count_to_file(row_count)

# Ejecutar el flujo
flow.run()
