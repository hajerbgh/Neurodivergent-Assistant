# Neurodivergent Assistant 

![Python](https://img.shields.io/badge/python-3.10+-blue?logo=python&logoColor=white) ![FastAPI](https://img.shields.io/badge/FastAPI-0.128.5-green?logo=fastapi&logoColor=white) ![HuggingFace](https://img.shields.io/badge/Hugging%20Face-Transformers-orange?logo=huggingface&logoColor=white)

**Version :** 1.0  
**Stack :** Python, FastAPI, Hugging Face Transformers (`facebook/bart-large-cnn`), Uvicorn  

---

##  Description

Neurodivergent Assistant est une API REST qui **résume automatiquement des textes en anglais**. Elle utilise le modèle **facebook/bart-large-cnn** pour produire des résumés précis et compréhensibles, parfait pour la lecture rapide d’articles, notes ou documents longs.

---

##  Fonctionnalités

- Résumé automatique de textes en anglais.  
- API REST simple à utiliser.  
- Swagger UI pour tester l’API facilement (`/docs`).  
- Extensible pour d’autres fonctionnalités NLP (traduction, génération de texte, etc.).  

---

## 📂 Structure du projet



Arborescence du projet
ai-neurodivergent-assistant/
│
├── app/
│   ├── main.py           # Application FastAPI
│   ├── test.py           # Script Python pour tester l'API
│   └── __init__.py
│
├── venv/                 # Environnement virtuel Python
├── requirements.txt      # Dépendances Python
└── README.md             # Ce fichier


---

## ⚡ Installation

1. **Cloner le dépôt :**

```bash
git clone  https://github.com/hajerbgh/Neurodivergent-Assistant
cd ai-neurodivergent-assistant



** Créer un environnement virtuel : **

python -m venv venv



Activer l’environnement :

Windows PowerShell :

.\venv\Scripts\Activate.ps1


Windows CMD :

venv\Scripts\activate.bat


Linux / MacOS :

source venv/bin/activate


Installer les dépendances :

pip install -r requirements.txt

Lancer le projet
uvicorn app.main:app --reload


L’API sera disponible sur : http://127.0.0.1:8000

Swagger UI pour tester l’API : http://127.0.0.1:8000/docs

Exemple d’utilisation via API

Endpoint : POST /summarize

Request JSON :

{
  "text": "I want to start learning tech fields such as AI, IoT, DevOps, and cybersecurity because there is a high demand for engineers worldwide."
}


Réponse JSON :

{
  "summary": "I want to start learning tech fields such as AI, IoT, DevOps, and cybersecurity due to high global demand for engineers."
}

Exemple d’utilisation avec test.py
import requests

url = "http://127.0.0.1:8000/summarize"
data = {"text": "I want to start learning tech fields such as AI, IoT, DevOps, and cybersecurity because there is a high demand for engineers worldwide."}

response = requests.post(url, json=data)
print("Résumé :", response.json()["summary"])

Technologies utilisées

Python 3.10+

FastAPI : framework pour créer l’API REST

Uvicorn : serveur ASGI rapide

Hugging Face Transformers : modèle facebook/bart-large-cnn pour le résumé

Requests : pour tester l’API
