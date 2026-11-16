from transformers import AutoModelForSequenceClassification, AutoTokenizer
import json
import torch

MODEL_PATH = "banking77_distilbert_final"

with open("id_to_label.json", "r", encoding="utf-8") as file:
    id_to_label = json.load(file)

model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model.eval()

def distilbert_predict(query: str):
    with torch.inference_mode():
        input = tokenizer(query, truncation=True, max_length=128, return_tensors="pt")
        logit = model(**input).logits
    prediction = logit.argmax(dim=-1).item()
    label = id_to_label[str(prediction)]
    return label
