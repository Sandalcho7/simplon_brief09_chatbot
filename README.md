# SIMPLON DEV IA | Brief 9

## Chatbot et data scraping

### Contexte

Dans le cadre de ma formation développeur IA chez Simplon, j'ai mis en place un chatbot avec lequel on peut intéragir via un frontend. Le contenu de ce frontend (simple, pour l'exercice) est scrapé et les données sont utilisées par le chatbot, si nécessaire, pour répondre aux questions.

### Structure du projet

```bash
project/
│
├── .github
│   └── workflows/
│       └── main-deployment.yml    # Deployments config for pull requests on main branch
│
├── backend/
│   ├── chatbot.py    # Chatbot function (uses Eden AI service)
│   ├── config.py    # API settings (mostly Eden AI), API key here
│   ├── Dockerfile
│   ├── main.py    # API script
│   ├── mini_bot.py    # Bot with history (exercise)
│   ├── requirements.txt
│   └── scraper.py    # Web scraping (used in API script)
│
├── site/
│   ├── assets/
│   │   └── images/    # Website images
│   ├── Dockerfile
│   ├── index.html
│   ├── script.js
│   └── style.css
│
├── tests/
│   └── test_chatbot.py
│
├── .gitignore
├── config_deploy_main.yml    # Containers instance configuration
└── README.md
```

### Notes

Ce projet a été développé pour être déployé sur Azure via Github Actions, il est cependant possible de le faire tourner en local avec la procédure renseignée en fin de README.

### CI/CD sur Azure <hr>

### Prérequis pour le déploiement continu sur Azure

- Un compte [Microsoft Azure](https://portal.azure.com/)<br><br>
- Un compte [Eden AI](https://app.edenai.run/)<br><br>
- Azure CLI installée sur votre machine (nécéssaire pour utiliser les commandes ci-dessous)

### Procédure (celle que j'ai suivie en tout cas)

0 / Cloner le projet sur un repo GitHub personnel<br>

1 / Depuis votre CLI, connectez votre compte Azure (avec cette commande, une page web devrait s'ouvrir pour renseigner vos identifiants) :
```bash
az login
```

2 / Maintenant, il s'agit de créer un groupe de ressources :
```bash
az group create --name <resource-group-name> --location westeurope
```

3 / La prochaine étape est de créer un service principal :
```bash
az ad sp create-for-rbac --name "<service-principal-name>" --role contributor --scopes <Resource-ID> --json-auth
```
Notez que le nom du service principal doit être renseigné entre "quotes", le Resource ID est trouvable depuis le portail Azure, dans les propriétés de votre groupe de ressources.<br>

4 / La commande précédente devrait renvoyer un dictionnaire avec vos credentials (pour ce service principal), ajoutez-le en tant que AZURE_CREDENTIALS dans les secrets GitHub (dans votre repo : Settings > Secrets and variables > Actions > New repository secret).
```bash
{
  "clientId": "7cfda...",
  "clientSecret": "kyc5...",
  "subscriptionId": "u7ef8...",
  "tenantId": "b4e496...",
  "activeDirectoryEndpointUrl": "https://login.microsoftonline.com/",
  "resourceManagerEndpointUrl": "https://management.azure.com/",
  "activeDirectoryGraphResourceId": "https://graph.windows.net/",
  "sqlManagementEndpointUrl": "https://management.core.windows.net:8443/",
  "galleryEndpointUrl": "https://gallery.azure.com/",
  "managementEndpointUrl": "https://management.core.windows.net/"
}
```

5 / La prochaine étape est de créer un registre de conteneurs :
```bash
az acr create --resource-group <resource-group-name> --name <registry-name> --sku Standard
```

6 / Une fois le registre créé, rendez-vous sur le portail Azure et accédez à la rubrique "Access keys" de ce registre. Cochez la case "Admin user" et copier le premier mot de passe affiché. Ajoutez-le en tant que AZURE_ACR_PASSWORD dans les secrets GitHub.<br>

7 / Un dernier secret à créer est la clé Eden AI pour utiliser leur API. Une fois le compte gratuit créé, copier votre API Key et ajoutez-la en tant que EDEN_AI_KEY dans les secrets GitHub.<br>

8 / Il ne reste plus qu'à configurer votre API dans le fichier config.py puis configurer le déploiement dans les deux fichiers .yml présents dans le repo.<br>

9 / Une dernière étape avant le déploiement est de modifier l'adresse de l'API dans le fichier script.js (à faire après configuration du déploiement car l'URL dépend du DNS et de la région choisis). Une URL attendue pour un déploiement en région "westeurope" serait :
```js
const API_PATH = 'http://<dns-name-label>.westeurope.azurecontainer.io:<port>/'
```

### Fonctionnement en local <hr>

### Prérequis

- Un compte [Eden AI](https://app.edenai.run/)

### Procédure

1 / Avant de démarrer le projet, il est nécessaire d'installer certaines dépendances sur l'environnement de travail. Pour effectuer ces installations, vous pouvez éxécuter la commande suivante :
```bash
pip install -r backend/requirements.txt
```

2 / Accédez à votre compte Eden AI et copiez votre API key, renseignez-la dans le fichier config.py :
```py
KEY = "eyJhbG..."
```

3 / Pour modifier l'URL du site à scraper, modifiez SCRAPED_URL dans config.py :
```py
SCRAPED_URL = 'http://localhost:8001/'
```

4 / Il vous faudra aussi remplacer l'URL de l'API dans le script.js :
```js
const API_PATH = 'http://localhost:8000/'
```

5 / Depuis le terminal, se placer dans le dossier site/ et exécuter cette ligne de commande :
```bash
python -m http.server 8001
```

6 / Depuis le terminal, lancer l'API en se plaçant dans le dossier backend/ et en exécutant :
```bash
python main.py
```

7 / Se rendre à l'adresse http://localhost:8001 pour consulter la page et dialoguer avec le bot. Rafraîchir la page si besoin.
