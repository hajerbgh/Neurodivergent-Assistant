import requests

url = "http://127.0.0.1:8000/summarize"

data = {
    "text": "OpenAI a développé des modèles de langage avancés qui peuvent comprendre et générer du texte. "
            "Ces modèles sont utilisés pour la traduction, le résumé, la génération de code et bien d'autres applications."
}

response = requests.post(url, json=data)

if response.status_code == 200:
    print("Résumé :", response.json()["summary"])
else:
    print("Erreur :", response.status_code, response.text)
