# timedelta_convert.py
import json
import random
import spacy
from spacy.tokens import DocBin

IN = "raw_data.jsonl"
OUT_TRAIN = "train.spacy"
OUT_DEV = "dev.spacy"
DEV_RATIO = 0.15
LANG = "es"

examples = []
try:
    with open(IN, "r", encoding="utf8") as f:
        data = json.load(f)
        if isinstance(data, list):
            for item in data:
                if isinstance(item, list) and len(item) == 2:
                    text, cats_dict = item
                    examples.append((text, cats_dict))
                else:
                    print(f"WARNING: Invalid data format in item: {item}")
        else:
            print("ERROR: Expected a list at top level.")
            exit(1)
except FileNotFoundError:
    print(f"ERROR: File {IN} not found.")
    exit(1)
except json.JSONDecodeError as e:
    print(f"ERROR: JSON decode error: {e}")
    exit(1)

if not examples:
    print("ERROR: No valid examples loaded.")
    exit(1)

nlp = spacy.blank(LANG)
random.shuffle(examples)
split_idx = int(len(examples) * (1 - DEV_RATIO))
train_ex = examples[:split_idx]
dev_ex = examples[split_idx:]

def make_docbin(list_examples, out_path):
    db = DocBin(store_user_data=True)
    for text, cats_dict in list_examples:
        doc = nlp.make_doc(text)
        # Set cats directly from the provided dictionary
        doc.cats = cats_dict.get("cats", {})

        # No entities to process
        db.add(doc)
    db.to_disk(out_path)
    print(f"Wrote {out_path} ({len(list_examples)} examples)")

make_docbin(train_ex, OUT_TRAIN)
make_docbin(dev_ex, OUT_DEV)