# GameRecommender

Application de recommandation de jeux vidéo, combinant un modèle de recommandation (Machine Learning) avec une interface web simple.

## 🎮 Aperçu

GameRecommender analyse les préférences ou l'historique de l'utilisateur pour lui suggérer des jeux vidéo pertinents, via un modèle de recommandation entraîné sur des données de jeux.

## 🗂️ Structure du projet

```
GameRecommender/
├── ai/         # Modèle de recommandation (Machine Learning)
├── backend/    # Serveur / API
├── data/       # Jeux de données utilisés pour entraîner et alimenter le modèle
└── frontend/   # Interface utilisateur (HTML/CSS/JS)
```

- **`ai/`** — Contient le modèle de recommandation : entraînement, inférence, et logique de scoring des jeux en fonction du profil utilisateur.
- **`backend/`** — Sert d'API entre le frontend et le modèle IA, gère les requêtes et transmet les recommandations.
- **`data/`** — Données brutes et/ou pré-traitées utilisées par le modèle (catalogues de jeux, notes, historiques d'utilisation, etc.).
- **`frontend/`** — Interface web en HTML/CSS/JavaScript permettant à l'utilisateur d'interagir avec le système de recommandation.

## 🚀 Installation

> ⚠️ Section à compléter selon la stack exacte du backend (Python/Flask, Node.js, etc.)

```bash
# Cloner le repo
git clone https://github.com/Equinoxya/GameRecommender.git
cd GameRecommender

# Installer les dépendances du backend
# (à préciser selon le langage utilisé)

# Lancer le backend
# ...

# Ouvrir le frontend
# Ouvrir frontend/index.html dans un navigateur, ou servir via un serveur local
```

## 🧠 Modèle de recommandation

Le dossier `ai/` contient la logique du système de recommandation. Il s'appuie sur les données du dossier `data/` pour proposer des jeux pertinents à l'utilisateur.

*(Précise ici l'algorithme utilisé — filtrage collaboratif, content-based, hybride, etc. — pour compléter cette section.)*

## 🛠️ Stack technique

| Composant  | Technologie |
|------------|-------------|
| Frontend   | HTML / CSS / JavaScript |
| Backend    | À préciser |
| IA / ML    | À préciser (scikit-learn, etc.) |
| Données    | À préciser (format des fichiers dans `data/`) |

## 📄 Licence

Aucune licence spécifiée pour le moment.

## ✍️ Auteur

[Equinoxya](https://github.com/Equinoxya)
