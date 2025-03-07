# EN

# **Monstropedia**

Monstropedia is a tool that allows users to search, create, and manage monster characteristics through a one-page interface. This project uses **VueJS** for the front-end and **FastAPI** for the back-end.

---

## **Description**

Monstropedia enables users to manage monster data via a simple and clear interface. The tool primarily works with a **JSON** file that simulates a database for monster characteristics. However, please note that this file is **volatile** and loses modifications once the server is restarted.

---

## **Installation**

### Prerequisites

Before you begin, ensure you have the following tools installed:

- **Node.js** (for the front-end)
- **Python** (for the back-end)

### Installation Steps

1. **Clone the repository:**

    ```bash
    git clone https://github.com/GeoffreyValade/monstropedia.git
    ```

2. **Front-End**

    Navigate to the front-end folder, then install the dependencies and start the development server.

    ```bash
    cd frontend
    npm install
    npm run dev
    ```

3. **Back-End**

    Navigate to the back-end folder, install the dependencies, and start the application with **Uvicorn**.

    ```bash
    cd backend
    pip install -r requirements.txt
    python -m uvicorn main:app --reload
    ```

---

## **Usage**

The project offers the following features:

- **Retrieve JSON File**: You can retrieve monster data from the provided JSON file.
- **Write to Server's RAM**: Changes made to the monsters are temporarily stored in the server's RAM.
- **Delete Objects**: You can delete monsters that already exist in the JSON file.

### Limitations

- **No Writing to JSON File**: It is currently impossible to write directly to the JSON file from the application. Changes must be made manually in the JSON file.
- **JSON Simulating a Database**: The JSON file acts as a database but is not a true persistent database. Any changes will be lost after restarting the server.

---

## **Contributing**

Currently, this project does not accept external contributions.

---

## **Tests**

There are no unit tests defined for this project at the moment.

---

## **Licenses**

No license has been defined for this project yet. You can check the documentation for the technologies used for more information about their respective licenses.

---

## **Technologies Used**

- **VueJS**: JavaScript framework for the front-end.
- **Axios**: Library for making HTTP requests on the front-end.
- **FastAPI**: Python framework for building fast and modern APIs.
- **Uvicorn**: ASGI server for the back-end.

---

## **Authors**

- **Geoffrey Valade** – Creator and lead developer of the project.

---

## **Note**

If you'd like more information about the versions of **VueJS**, **FastAPI**, or **Uvicorn** used, you can check them in the configuration files:

- **`package.json`** for **VueJS** and **Axios**.
- **`requirements.txt`** for **FastAPI** and **Uvicorn**.


----------------------------------------------------------------------------------------------------------------------------------

# FR

# **Monstropedia**

Monstropedia est un outil qui permet aux utilisateurs de rechercher, créer et gérer les caractéristiques des monstres via une interface one-page. Ce projet utilise **VueJS** pour le front-end et **FastAPI** pour le back-end.

---

## **Description**

Monstropedia permet aux utilisateurs de gérer les données des monstres à travers une interface simple et claire. L'outil fonctionne principalement avec un fichier **JSON** qui simule une base de données pour les caractéristiques des monstres. Cependant, veuillez noter que ce fichier est **volatile** et perd les modifications une fois le serveur redémarré.

---

## **Installation**

### Prérequis

Avant de commencer, assurez-vous d'avoir installé les outils suivants :

- **Node.js** (pour le front-end)
- **Python** (pour le back-end)

### Étapes d'installation

1. **Clonez le dépôt :**

    ```bash
    git clone https://github.com/GeoffreyValade/monstropedia.git
    ```

2. **Front-End**

    Naviguez vers le dossier du front-end, puis installez les dépendances et lancez le serveur de développement.

    ```bash
    cd frontend
    npm install
    npm run dev
    ```

3. **Back-End**

    Naviguez vers le dossier du back-end, installez les dépendances, puis lancez l'application avec **Uvicorn**.

    ```bash
    cd backend
    pip install -r requirements.txt
    python -m uvicorn main:app --reload
    ```

---

## **Utilisation**

Le projet offre les fonctionnalités suivantes :

- **Récupérer le fichier JSON** : Vous pouvez récupérer les données des monstres depuis le fichier JSON fourni.
- **Écrire en mémoire vive du serveur** : Les modifications apportées aux monstres sont temporairement stockées en mémoire vive du serveur.
- **Supprimer des objets** : Vous pouvez supprimer des monstres déjà existants dans le fichier JSON.

### Limitations

- **Pas d'écriture dans le fichier JSON** : Il est actuellement impossible d'écrire directement dans le fichier JSON depuis l'application. Les modifications doivent être faites manuellement dans le fichier JSON.
- **JSON simulant une base de données** : Le fichier JSON agit comme une base de données mais ne constitue pas une véritable base de données persistante. Toute modification sera perdue après un redémarrage du serveur.

---

## **Contribuer**

Actuellement, ce projet n'accepte pas de contributions externes.

---

## **Tests**

Aucun test unitaire n'a été défini pour ce projet pour le moment.

---

## **Licences**

Aucune licence n'a encore été définie pour ce projet. Vous pouvez consulter la documentation des technologies utilisées pour plus d'informations sur leurs licences respectives.

---

## **Technologies utilisées**

- **VueJS** : Framework JavaScript pour le front-end.
- **Axios** : Bibliothèque pour effectuer des requêtes HTTP sur le front-end.
- **FastAPI** : Framework Python pour créer des APIs rapides et modernes.
- **Uvicorn** : Serveur ASGI pour le back-end.

---

## **Auteurs**

- **Geoffrey Valade** – Créateur et développeur principal du projet.

---

## **Note**

Si vous souhaitez plus d'informations sur les versions de **VueJS**, **FastAPI**, ou **Uvicorn** utilisées, vous pouvez les consulter dans les fichiers de configuration :

- **`package.json`** pour **VueJS** et **Axios**.
- **`requirements.txt`** pour **FastAPI** et **Uvicorn**.

