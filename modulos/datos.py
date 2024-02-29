import csv
import json


def csv_to_json(csv_file, json_file):
    # Lista para almacenar los datos del CSV
    data = []

    # Lee el archivo CSV y guarda los datos en la lista
    with open(csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)

    # Escribe los datos en un archivo JSON
    with open(json_file, 'w') as file:
        json.dump(data, file, indent=4)

# Nombre del archivo CSV de entrada
csv_file = 'libro-prueba.csv'

# Nombre del archivo JSON de salida
json_file = 'inventario.json'

# Llama a la función para convertir CSV a JSON
csv_to_json(csv_file, json_file)

print("Conversion completa.")

