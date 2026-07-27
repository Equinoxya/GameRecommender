from flask import Flask, request, jsonify
from sklearn.ensemble import RandomForestClassifier
import os

app = Flask(__name__)

# --- Dataset ---
# [age, heures_par_semaine, preference (1=solo, 2=multi), plateforme (1=mobile, 2=PC, 3=console)]
X = [
    [16, 20, 2, 2], [20, 15, 2, 2], [19, 25, 2, 2], [22, 18, 2, 2],
    [25, 10, 2, 3], [30, 5,  2, 3], [28, 8,  2, 3], [35, 6,  2, 3],
    [25, 20, 1, 2], [30, 15, 1, 2], [27, 18, 1, 2],
    [35, 10, 1, 2], [40, 8,  1, 2], [32, 45, 1, 2], [35, 40, 1, 2], [42, 12, 1, 2],
    [20, 5,  1, 1], [35, 3,  1, 1], [45, 2,  1, 1], [50, 4,  1, 1],
    [18, 25, 1, 3], [22, 20, 1, 3], [26, 15, 1, 3],
    [17, 30, 2, 2], [19, 28, 2, 2], [21, 22, 2, 1], [23, 20, 2, 1],
    [28, 25, 2, 2], [24, 30, 2, 2], [26, 28, 2, 2],
    [30, 10, 1, 1], [25, 8,  1, 1], [22, 12, 1, 1],
    [33, 15, 1, 2], [40, 10, 1, 2], [38, 12, 1, 2],
    [29, 20, 1, 3], [24, 18, 1, 3], [27, 22, 1, 3],
    [25, 15, 1, 2], [30, 10, 1, 2],
    [35, 12, 2, 2], [28, 20, 2, 2], [32, 18, 2, 2]
]

y = [
    "FPS", "FPS", "FPS", "FPS",
    "Sport", "Sport", "Sport", "Sport",
    "RPG", "RPG", "RPG",
    "Stratégie", "Stratégie", "Stratégie", "Stratégie", "Stratégie",
    "Casual", "Casual", "Casual", "Casual",
    "Aventure", "Aventure", "Aventure",
    "Battle Royale", "Battle Royale", "Battle Royale", "Battle Royale",
    "MOBA", "MOBA", "MOBA",
    "RPG Mobile", "RPG Mobile", "RPG Mobile",
    "Simulation", "Simulation", "Simulation",
    "JRPG", "JRPG", "JRPG",
    "Survival Horror", "Survival Horror",
    "MMO", "MMO", "MMO"
]

# Validation de la structure du dataset
assert len(X) == len(y), "X et y doivent avoir la même taille"

# --- Entraînement du modèle Random Forest ---
model = RandomForestClassifier(
    n_estimators=100,  # 100 arbres de décision combinés
    max_depth=5,       # Limite la profondeur pour éviter l'overfitting
    random_state=42    # Garantit des résultats reproductibles
)
model.fit(X, y)

@app.route('/health', methods=["GET"])
def health():
    return jsonify({"status": "Ok"}), 200

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "API IA opérationnelle (Random Forest)"}), 200

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(silent=True)
    
    # Sécurité : vérifier qu'un corps JSON valide a été envoyé
    if not data:
        return jsonify({"error": "Requête invalide, un body JSON est requis."}), 400

    # Parsing et valeurs par défaut
    age = data.get("age", 20)
    heures = data.get("heures_par_semaine", 5)
    
    pref_raw = str(data.get("preference", "")).lower()
    preference = 1 if pref_raw == "solo" else 2

    plateforme_map = {"mobile": 1, "pc": 2, "console": 3}
    plateforme_raw = str(data.get("plateforme", "")).lower()
    plateforme = plateforme_map.get(plateforme_raw, 2)

    # Prédictions
    features = [[age, heures, preference, plateforme]]
    prediction = model.predict(features)[0]
    proba = model.predict_proba(features)[0]

    # Détails des probabilités nettoyés
    classes = model.classes_
    proba_dict = {cls: round(float(p), 3) for cls, p in zip(classes, proba)}

    return jsonify({
        "genre_ia": prediction,
        "confiance": round(float(max(proba)), 3),
        "details": proba_dict
    }), 200

# Alignement avec le port d'hébergement (Render, Heroku, etc.)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)