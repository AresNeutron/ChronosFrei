import json

IN="raw_data.json"
OUT="data.json"
examples = None

with open(IN, "r", encoding="utf8") as f:
    examples = json.load(f)

def convert_to_spacy_format(data):
    training_data = []
    for example in data:
        text = example["text"]
        intent = example["intent"]
        entities = []
        for label, entity_value in example["entities_dict"].items():
            
            # --- LÓGICA AGREGADA ---
            # Si el valor de la entidad es una lista, iteramos sobre los fragmentos
            if isinstance(entity_value, list):
                for fragment in entity_value:
                    start_index = text.find(fragment)
                    if start_index != -1:
                        end_index = start_index + len(fragment)
                        entities.append({"start": start_index, "end": end_index, "label": label})
            # Si es una cadena de texto simple, usamos la lógica anterior
            else:
                start_index = text.find(entity_value)
                if start_index != -1:
                    end_index = start_index + len(entity_value)
                    entities.append({"start": start_index, "end": end_index, "label": label})
        
        spacy_format = {
            "text": text,
            "entities": entities,
            "intent": intent,
        }
        training_data.append(spacy_format)
    
    return training_data

converted_data = convert_to_spacy_format(examples)

try:
    with open(OUT, "r", encoding="utf-8") as f:
        existing_data = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    # Handle the case where the file doesn't exist or is empty/invalid
    existing_data = []

# Append the new data
existing_data.extend(converted_data)

# Write the entire list back to the file
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(existing_data, f, indent=2, ensure_ascii=False)

print("Datos nuevos agregados exitosamente a 'data.json'!")
