# Documentation des Outils Utilisés

Ce document décrit de manière détaillée tous les outils et technologies utilisés dans la réalisation de ce projet Portfolio Django.

## 🛠️ Environnement de Développement

- **Python** : Langage principal pour le développement backend.
- **Django** : Framework web utilisé pour structurer l'application (`manage.py`, applications Django, configuration dans le dossier `config`).
- **SQLite3** : Base de données légère utilisée en local (`db.sqlite3`).

## 📁 Structure du Projet

- `config/` : Contient les fichiers de configuration Django (`settings.py`, `urls.py`, etc.).
- `core/` : Application Django principale avec modèles, vues, tests et commandes personnalisées.
- `templates/` : Modèles HTML utilisés pour rendre les pages.
- `static/` : Fichiers CSS et images statiques.
- `media/` : Contenu téléversé (images de projets, blog, etc.).

## 🧱 Composants Django et Outils Spécifiques

- **Modèles (`models.py`)** : Représentation des entités (Post, Project, Skill, etc.).
- **Vues (`views.py`)** : Logique de rendu des pages et gestion des requêtes HTTP.
- **URLs (`urls.py`)** : Routage des URLs vers les vues correspondantes.
- **Administration (`admin.py`)** : Configuration de l’interface d’administration Django.
- **Context Processors (`context_processors.py`)** : Fournissent des données globales aux templates.
- **Gestionnaire de Commandes (`management/commands/seed_data.py`)** : Commande personnalisée pour remplir la base de données de données de test.
- **Migrations** : Gèrent l’évolution du schéma de la base de données.

## 📦 Fichiers de Configuration

- `requirements.txt` : Liste des dépendances Python utilisées (Django, etc.).

## ✒️ Templates HTML

Modèles pour:
- Page d’accueil, blog, projets, contact, CV, etc.
- Templates d’administration personnalisés.
- Includes partiels (`_navbar`, `_footer`).

## 🧩 Outils et Plugins Concernés (si applicables)

- **Django Admin** : Interface de gestion de contenu.
- **Staticfiles** : Collecte et servi de fichiers statiques en production.
- **URL dispatcher** de Django pour le routage dynamique.

## 💡 Conseils d'Utilisation

- Exécuter `python manage.py runserver` pour lancer le serveur local.
- Utiliser `python manage.py makemigrations` et `migrate` pour appliquer les modifications de schéma.
- Ajouter des dépendances dans `requirements.txt` et installer via `pip install -r requirements.txt`.

---

Ce document sert à donner une vue complète des outils et composants impliqués dans le développement du projet. Vous pouvez le compléter en cas d’ajout de nouveaux éléments.