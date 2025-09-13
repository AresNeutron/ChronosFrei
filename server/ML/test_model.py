import spacy

# Cargar el modelo entrenado
nlp = spacy.load("./models/model-last")

# Textos de prueba
test_texts = [
    "programa una reunión con el equipo mañana de 10:00 a 11:00",
    "¿qué tengo agendado para el viernes?",
    "agenda una cita con el doctor para la próxima semana de 9 AM a 10 AM",
    "muéstrame los eventos de hoy"
]

print("🧠 Probando el modelo entrenado...\n")

for text in test_texts:
    doc = nlp(text)
    
    print(f"📝 Texto: '{text}'")
    
    # Clasificación de intención
    print("🎯 Intención:", max(doc.cats, key=doc.cats.get), f"({doc.cats[max(doc.cats, key=doc.cats.get)]:.2f})")
    
    # Entidades extraídas
    print("🏷️  Entidades:")
    for ent in doc.ents:
        print(f"   - {ent.text} → {ent.label_}")
    
    print("-" * 60)