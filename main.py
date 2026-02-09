from fastapi import FastAPI
from app.models import TextInput
from transformers import BartForConditionalGeneration, BartTokenizer

# Nom du modèle
MODEL_NAME = "facebook/bart-large-cnn"

# Charger le tokenizer et le modèle
tokenizer = BartTokenizer.from_pretrained(MODEL_NAME)
model = BartForConditionalGeneration.from_pretrained(MODEL_NAME)

# Créer l'application FastAPI
app = FastAPI(
    title="AI Neurodivergent Assistant",
    description="API pour résumer du texte avec facebook/bart-large-cnn",
    version="1.0"
)

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API de résumé de texte !"}

@app.post("/summarize")
def summarize_text(input: TextInput):
    # Tokenisation
    inputs = tokenizer.encode(input.text, return_tensors="pt", max_length=1024, truncation=True)
    
    # Génération du résumé
    summary_ids = model.generate(
        inputs, 
        max_length=150, 
        min_length=40, 
        length_penalty=2.0, 
        num_beams=4, 
        early_stopping=True
    )
    
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return {"summary": summary}
