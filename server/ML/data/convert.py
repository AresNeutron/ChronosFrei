# convert_to_spacy.py
import json, random
import spacy
from spacy.tokens import DocBin

IN = "combined_training_data.json"
OUT_TRAIN = "train.spacy"
OUT_DEV = "dev.spacy"
DEV_RATIO = 0.15
LANG = "es"

with open(IN, "r", encoding="utf8") as f:
    examples = json.load(f)

# Recolectar todos los intents
all_intents = sorted(list({ex["intent"] for ex in examples}))

nlp = spacy.blank(LANG)
random.shuffle(examples)
split_idx = int(len(examples) * (1 - DEV_RATIO))
train_ex = examples[:split_idx]
dev_ex = examples[split_idx:]

def make_docbin(list_examples, out_path):
    db = DocBin(store_user_data=True)
    for ex in list_examples:
        doc = nlp.make_doc(ex["text"])
        # cats (one-hot)
        cats = {it: 1.0 if it == ex["intent"] else 0.0 for it in all_intents}
        doc.cats = cats

        spans = []
        for e in ex.get("entities", []):
            s, ee, label = e["start"], e["end"], e["label"]
            span = doc.char_span(s, ee, label=label, alignment_mode="expand")  # probar expand para más tolerancia
            if span is None:
                print(f"WARNING: No se pudo alinear span en texto: {ex['text']!r} -> {s}:{ee} label={label}")
            else:
                spans.append(span)
        if spans:
            # spaCy exige que doc.ents no se solapen; si hay solapamiento, drop o revisar
            try:
                doc.ents = spans
            except Exception as err:
                print("ERROR asignando ents:", err)
                # Aquí podrías filtrar spans solapados manualmente
        db.add(doc)
    db.to_disk(out_path)
    print(f"Wrote {out_path} ({len(list_examples)} examples)")

make_docbin(train_ex, OUT_TRAIN)
make_docbin(dev_ex, OUT_DEV)
