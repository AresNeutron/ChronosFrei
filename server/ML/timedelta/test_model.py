import spacy

def main():
    try:
        nlp = spacy.load('./output/model-best')
        test_phrases = [
            "dentro de 5 minutos",
            "el próximo lunes",
            "dentro de una semana",
            "en dos horas",
            "por la tarde"
        ]
        for phrase in test_phrases:
            doc = nlp(phrase)
            cats = doc.cats
            # Find the category with highest score
            predicted_cat = max(cats, key=cats.get)
            confidence = cats[predicted_cat]
            print(f"Phrase: '{phrase}' -> Category: {predicted_cat}, Confidence: {confidence:.4f}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()