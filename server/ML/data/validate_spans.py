import json

# Nombre del archivo
file_name = "data.json"

try:
    # Abrir y cargar los datos del archivo JSON
    with open(file_name, 'r', encoding= 'utf-8') as file:
        data_list = json.load(file)

    # Iterar sobre cada objeto en la lista
    for item in data_list:
        text = item["text"]
        entities = item["entities"]
        print(f'Texto original: "{text}"')
        
        # Iterar sobre cada entidad y extraer el fragmento de texto
        for entity in entities:
            start = entity["start"]
            end = entity["end"]
            fragment = text[start:end]
            label = entity["label"]
            print(f'  - Fragmento: "{fragment}" (Etiqueta: {label})')
        print("-" * 30)

except FileNotFoundError:
    print(f"Error: El archivo '{file_name}' no se encontró.")
except json.JSONDecodeError:
    print(f"Error: No se pudo decodificar el archivo '{file_name}'. Asegúrate de que es un JSON válido.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")