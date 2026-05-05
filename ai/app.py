from flask import Flask, request, jsonify
from sklearn.tree import DecisionTreeClassifier
import os

app = Flask(__name__)

# Dataset
# [age, heures_par_semaine, preference (1=solo, 2=multi), plateforme (1=mobile, 2=PC, 3=console)]
X = [
    [16, 20, 2, 2],  # FPS
    [20, 15, 2, 2],  # FPS
    [25, 10, 2, 3],  # Sport
    [30, 5,  2, 3],  # Sport
    [25, 20, 1, 2],  # RPG
    [30, 15, 1, 2],  # RPG
    [35, 10, 1, 2],  # Stratégie
    [40, 8,  1, 2],  # Stratégie
    [32, 45, 1, 2],  # Stratégie
    [35, 40, 1, 2],  # Stratégie
    [20, 5,  1, 1],  # Casual
    [35, 3,  1, 1],  # Casual
    [18, 25, 1, 3],  # Aventure
    [22, 20, 1, 3],  # Aventure
]

y = [
    "FPS", "FPS",
    "Sport", "Sport",
    "RPG", "RPG",
    "Stratégie", "Stratégie",
    "Stratégie", "Stratégie",
    "Casual", "Casual",
    "Aventure", "Aventure"
]

# Sécurité : vérifier cohérence dataset
assert len(X) == len(y), "X et y doivent avoir la même taille"

# Modèle
model = DecisionTreeClassifier()
model.fit(X, y)
@app.route('/health')
def health():
    return {"status" : "Ok"}
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "API IA opérationnelle"})


@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    age = data.get("age", 20)
    heures = data.get("heures_par_semaine", 5)
    preference = 1 if data.get("preference") == "solo" else 2
    plateforme = {
        "mobile": 1,
        "PC": 2,
        "console": 3
    }.get(data.get("plateforme"), 2)

    # Prédiction
    prediction = model.predict([[age, heures, preference, plateforme]])
    proba = model.predict_proba([[age, heures, preference, plateforme]])

    # Détail des probabilités
    classes = model.classes_
    proba_dict = dict(zip(classes, proba[0]))

    return jsonify({
        "genre_ia": prediction[0],
        "confiance": float(max(proba[0])),
        "details": proba_dict
    })


# Lancement compatible Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)