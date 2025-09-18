import json

IN="raw_data.json"
examples = None

with open(IN, "r", encoding="utf8") as f:
    examples = json.load(f)

def convert_to_spacy_format(data):
    training_data = []
    for example in data:
        text = example["text"]
        intent = example["intent"]
        entities = []
        for label, entity_text in example["entities_dict"].items():
            start_index = text.find(entity_text)
            if start_index != -1:
                end_index = start_index + len(entity_text)
                entities.append((start_index, end_index, label))
            # Opcionalmente, agrega lógica para manejar múltiples ocurrencias
        
        # Genera el JSON final para spaCy
        spacy_format = {
            "text": text,
            "entities": [{"start": s, "end": e, "label": l} for s, e, l in entities],
            "intent": intent,
        }
        training_data.append(spacy_format)

    return training_data

converted_data = convert_to_spacy_format(examples)

try:
    with open("data.json", "r", encoding="utf-8") as f:
        existing_data = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    # Handle the case where the file doesn't exist or is empty/invalid
    existing_data = []

# Append the new data
existing_data.extend(converted_data)

# Write the entire list back to the file
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(existing_data, f, indent=2, ensure_ascii=False)

print("Datos nuevos agregados exitosamente a 'data.json'!")
