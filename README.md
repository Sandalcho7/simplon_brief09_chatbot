# SIMPLON DEV IA | Brief 9

## Intégrer un chatbot IA à son portfolio

### Contexte

En tant que développeur IA, je suis chargé d'intégrer un chatbot dans un site web existant. Le chatbot sera alimenté par une API externe (Mistral, OpenAI, Bard, Anthropic...) pour fournir des réponses conversationnelles aux utilisateurs du site.

### Structure du projet

```bash
project/
│
├── fast_api/
│   ├── keys/
│   │   └── key.py    # API key placeholder
│   ├── main.py    # API script
│   ├── mini_bot.py    # Bot with history (exercise)
│   ├── requirements.txt    # Used to install all the project dependencies
│   └── scraper.py    # Web scraping (used in API script)
│
├── site/
│   ├── assets/
│   │   ├── images/    # Website images
│   │   ├── chatbot.js    # Chatbot script
│   │   └── style.css    # Website styling
│   └── index.html    # Website content
│
├── .gitignore
├── README.md
└── requirements.txt    # Used to install all the project dependencies
```

### Prérequis

Avant de démarrer le projet, il est nécessaire d'installer certaines dépendances sur l'environnement de travail. Pour effectuer ces installations, vous pouvez éxécuter la commande suivante :
```bash
pip install -r requirements.txt
```
La clé API étant personnelle, il vous sera nécéssaire d'en founir une pour faire tourner le projet. Si vous en avez une en votre possession, placez-la en tant que variable dans un fichier à l'emplacement fast_api/keys/key.py.
```py
key = 'insérer votre clé ici'
```

### Notes

J'ai fait le choix d'utiliser Eden AI en tant qu'API vers des modèles de mon choix. Dans le code fourni, le modèle est celui de Mistral, pour ses performances adaptées à l'utilisation faite ici mais aussi pour son coût relativement peu élevé.<br><br>
Si vous souhaitez changer de modèle, il suffit de modifier la valeur de 'provider' dans le fichier fast_api/main.py

### Procédure

1 / Depuis le terminal, se placer à la racine du projet et exécuter cette ligne de commande :
```bash
python -m http.server 8001
```
2 / Depuis le terminal, lancer l'API en se plaçant dans le dossier fast_api et en exécutant :
```bash
python3 main.py
```
Le script de web scraping sera automatiquement executé, si vous souhaitez changer l'url à scraper, modifiez la variable url dans le fichier fast_api/scraper.py<br><br>
3 / Se rendre à l'adresse http://localhost:8001 pour consulter la page et dialoguer avec le bot. Rafraîchir la page si besoin.
