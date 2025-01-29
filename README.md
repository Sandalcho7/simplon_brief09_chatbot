# Frontend et chatbot personnalisé

## Contexte
Dans le cadre de ma formation développeur IA chez Simplon, j'ai mis en place un chatbot avec lequel on peut intéragir via un frontend. Le contenu de ce frontend (simple et sans réel but, pour l'exercice) est scrapé et les données sont utilisées par le chatbot, si nécessaire, pour répondre aux questions. Ce projet impliquant un backend et un frontend m'a aussi permis de faire mes premiers pas avec Docker.

## Structure du projet
```bash
project/
│
├── src/
│	├── backend/
│	│   ├── chatbot.py			# Fonction et configuration du chatbot
│	│   ├── main.py    			# Script de l'API du chatbot
│	│   ├── mini_bot.py    		# Petit script de chat utilisable indépendamment (exercice)
│	│   └── scraper.py    		# Fonction de scraping du frontend
│	│
│	└── frontend/
│	    ├── assets/
│	    │   └── images/    		# Images du site web
│	    ├── index.html
│	    ├── script.js
│	    └── style.css
│
├── .env
├── .gitignore
├── docker-compose.yml
├── Dockerfile.back
├── Dockerfile.front
├── README.md
├── requirements.txt
└── template.env				# Template pour le fichier .env contenant la clé API
```

## Prérequis avant le lancement via Docker
- Installation de Docker
- Une clé API [Eden AI](https://app.edenai.run/)

## Procédure
1 / Création du fichier .env à la racine du projet en suivant le template :
```py
EDENAI_KEY=""
```

2 / Déploiement en local grâce au `docker-compose.yml`, en vous plaçant à la racine du projet, exécutez :
```bash
docker-compose up
```

3 / Se rendre à l'adresse http://localhost:8001 pour consulter la page et dialoguer avec le bot.