Voici une **version mieux structurée, plus lisible et plus professionnelle**, sans emojis. La hiérarchie des titres est plus claire et la lecture est plus fluide, comme dans une vraie documentation technique.

---

# Documentation des Outils Utilisés

## 1. Introduction

Ce document présente les outils et technologies utilisés pour le développement de ce projet **Portfolio basé sur Django**.
Il décrit l’environnement de développement, l’organisation du projet ainsi que les principaux composants utilisés dans l’application.

L’objectif est de fournir une vue d’ensemble claire de l’architecture du projet afin de faciliter sa compréhension, sa maintenance et son évolution.

---

# 2. Environnement de Développement

Le projet repose principalement sur les technologies suivantes :

**Python**
Langage principal utilisé pour développer toute la logique backend de l’application.

**Django**
Framework web Python qui structure l’application et facilite la gestion des modèles, des vues, des templates et du routage des URLs.

**SQLite3**
Base de données utilisée durant la phase de développement. Elle est simple à configurer et adaptée pour les projets locaux ou les prototypes.

---

# 3. Structure du Projet

Le projet suit l’organisation standard d’une application Django.

## 3.1 Dossier de configuration

**config/**
Ce dossier contient les fichiers de configuration globale du projet Django :

* `settings.py` : configuration principale du projet
* `urls.py` : routage principal des URLs
* `asgi.py` et `wsgi.py` : points d’entrée utilisés pour le déploiement de l’application

## 3.2 Application principale

**core/**
Il s’agit de l’application principale du projet. Elle contient notamment :

* les modèles de données
* les vues
* les tests
* certaines commandes personnalisées

## 3.3 Templates

**templates/**
Ce dossier regroupe tous les fichiers HTML utilisés pour générer les pages du site.

Les pages principales incluent par exemple :

* la page d’accueil
* la page des projets
* la section blog
* la page de contact
* la page CV

Certains éléments communs comme la barre de navigation ou le pied de page sont organisés sous forme de **templates partiels** afin de faciliter leur réutilisation.

## 3.4 Fichiers statiques

**static/**
Ce dossier contient les ressources statiques utilisées par l’application :

* feuilles de style CSS
* images
* fichiers JavaScript éventuels

## 3.5 Fichiers médias

**media/**
Ce dossier est utilisé pour stocker les fichiers téléversés par les utilisateurs, par exemple :

* images des projets
* images des articles du blog
* autres contenus uploadés

---

# 4. Composants Django Utilisés

## 4.1 Modèles

**models.py**

Les modèles représentent les différentes entités de l’application dans la base de données.
Chaque modèle correspond à une table dans la base.

Exemples d’entités possibles :

* articles de blog
* projets
* compétences

## 4.2 Vues

**views.py**

Les vues contiennent la logique applicative qui permet :

* de traiter les requêtes HTTP
* de récupérer les données depuis la base de données
* de retourner les pages HTML correspondantes

## 4.3 Routage des URLs

**urls.py**

Le fichier `urls.py` définit les routes du site et les associe aux vues correspondantes.

Par exemple :

* `/` pour la page d’accueil
* `/projects/` pour la liste des projets
* `/blog/` pour les articles

## 4.4 Interface d’administration

**admin.py**

Django fournit une interface d’administration intégrée qui permet de gérer facilement le contenu du site :

* création de projets
* publication d’articles
* modification des données

## 4.5 Context Processors

**context_processors.py**

Les context processors permettent de rendre certaines données accessibles dans tous les templates de l’application.

Cela est utile pour afficher des informations globales dans plusieurs pages du site.

## 4.6 Commandes personnalisées

**management/commands/seed_data.py**

Une commande Django personnalisée est utilisée pour générer rapidement des données de test dans la base de données.
Cela permet de remplir automatiquement l’application avec du contenu pendant le développement.

## 4.7 Migrations

Les migrations permettent de gérer l’évolution de la structure de la base de données lorsque les modèles sont modifiés.

---

# 5. Fichiers de Configuration

**requirements.txt**

Ce fichier contient la liste des dépendances Python nécessaires au projet, notamment Django et les bibliothèques supplémentaires utilisées dans l’application.

---

# 6. Gestion des Templates HTML

Les templates HTML sont utilisés pour générer dynamiquement les pages du site.

Certaines parties communes sont organisées en **templates partiels** afin d’éviter la duplication de code :

* `_navbar`
* `_footer`

Ces éléments sont ensuite inclus dans les templates principaux.

---

# 7. Outils et Fonctionnalités Django Utilisés

**Django Admin**

Interface intégrée permettant de gérer les contenus du site via un tableau de bord.

**Staticfiles**

Système utilisé par Django pour collecter et servir les fichiers statiques en environnement de production.

**URL Dispatcher**

Mécanisme de Django qui permet d’associer dynamiquement les URLs aux vues correspondantes.

---

# 8. Commandes Utiles

Lancer le serveur de développement :

```
python manage.py runserver
```

Créer des migrations après modification des modèles :

```
python manage.py makemigrations
```

Appliquer les migrations à la base de données :

```
python manage.py migrate
```

Installer les dépendances du projet :

```
pip install -r requirements.txt
```

---
