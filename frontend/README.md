<!-- language-all: lang=en -->

# **Monstropedia**

Monstropedia is a tool that allows users to search, create, and manage monster characteristics through a simple, one-page interface. This project uses **VueJS** for the front-end and **FastAPI** for the back-end.

---

## **Description**

Monstropedia allows users to manage monster data through an intuitive and clean interface. The tool primarily uses a **JSON** file that simulates a database for storing monster characteristics. However, please note that this file is **volatile**. Any changes made to the data will be lost upon server restart, as the changes are stored in memory.

---

## **Installation**

### **Prerequisites**

Before getting started, ensure you have the following tools installed:

- **Node.js** (for the front-end)
- **Python** (for the back-end)

### **Installation Steps**

1. **Clone the repository:**

    ```bash
    git clone https://github.com/GeoffreyValade/monstropedia.git
    ```

2. **Front-End**

    Navigate to the front-end folder, then install the dependencies and start the development server:

    ```bash
    cd frontend
    npm install
    npm run dev
    ```

3. **Back-End**

    Navigate to the back-end folder, install the dependencies, and start the application with **Uvicorn**:

    ```bash
    cd backend
    pip install -r requirements.txt
    python -m uvicorn main:app --reload
    ```

---

## **Usage**

The project provides the following features:

- **Retrieve Monster Data**: Fetch monster data from the provided JSON file.
- **Temporary Storage**: Any modifications made to the monsters are temporarily stored in the server's memory (RAM). These changes will not persist after a server restart.
- **Delete Monsters**: You can remove monsters that already exist in the JSON file.

### **Limitations**

- **No Direct Write to JSON File**: Currently, it is impossible to write directly to the JSON file from the application. If you need to save changes permanently, you must manually update the JSON file.
- **Volatile Data Storage**: The JSON file serves as a temporary data store. All changes made in the application are stored in RAM and will be lost when the server is restarted.

---

## **Contributing**

Currently, this project does not accept external contributions. However, feel free to fork the repository and make your own modifications.

---

## **Tests**

There are no unit tests defined for this project at the moment. Contributions in this area are welcome!

---

## **Licenses**

No official license has been defined for this project. For the respective licenses of the technologies used, refer to their official documentation:

- **VueJS**: [VueJS License](https://vuejs.org/)
- **FastAPI**: [FastAPI License](https://fastapi.tiangolo.com/)
- **Uvicorn**: [Uvicorn License](https://www.uvicorn.org/)

---

## **Technologies Used**

- **VueJS**: A JavaScript framework for building user interfaces.
- **Axios**: A library for making HTTP requests, used in the front-end for interacting with the back-end.
- **FastAPI**: A Python framework for building fast and modern APIs.
- **Uvicorn**: An ASGI server to run the FastAPI application.

---

## **Authors**

- **Geoffrey Valade** – Creator and lead developer of the project.

---

## **Note**

If you'd like to learn more about the specific versions of **VueJS**, **FastAPI**, or **Uvicorn** used in the project, you can check the following configuration files:

- **`package.json`** for **VueJS** and **Axios** versions.
- **`requirements.txt`** for **FastAPI** and **Uvicorn** versions.

----------------------------------------------------------


<!-- language-all: lang=fr -->

# **Monstropedia**

Monstropedia est un outil permettant aux utilisateurs de rechercher, créer et gérer les caractéristiques des monstres via une interface simple sur une seule page. Ce projet utilise **VueJS** pour le front-end et **FastAPI** pour le back-end.

---

## **Description**

Monstropedia permet aux utilisateurs de gérer les données des monstres via une interface intuitive et claire. L'outil utilise principalement un fichier **JSON** qui simule une base de données pour stocker les caractéristiques des monstres. Cependant, il est important de noter que ce fichier est **volatile**. Toutes les modifications apportées aux données seront perdues lors du redémarrage du serveur, car les modifications sont stockées en mémoire.

---

## **Installation**

### **Prérequis**

Avant de commencer, assurez-vous d'avoir les outils suivants installés :

- **Node.js** (pour le front-end)
- **Python** (pour le back-end)

### **Étapes d'installation**

1. **Clonez le dépôt :**

    ```bash
    git clone https://github.com/GeoffreyValade/monstropedia.git
    ```

2. **Front-End**

    Allez dans le dossier du front-end, puis installez les dépendances et lancez le serveur de développement :

    ```bash
    cd frontend
    npm install
    npm run dev
    ```

3. **Back-End**

    Allez dans le dossier du back-end, installez les dépendances et lancez l'application avec **Uvicorn** :

    ```bash
    cd backend
    pip install -r requirements.txt
    python -m uvicorn main:app --reload
    ```

---

## **Utilisation**

Le projet propose les fonctionnalités suivantes :

- **Récupérer les données des monstres** : Récupérez les données des monstres à partir du fichier JSON fourni.
- **Stockage temporaire** : Toute modification apportée aux monstres est stockée temporairement dans la mémoire (RAM) du serveur. Ces modifications ne persisteront pas après un redémarrage du serveur.
- **Supprimer des monstres** : Vous pouvez supprimer les monstres déjà présents dans le fichier JSON.

### **Limitations**

- **Pas d'écriture directe dans le fichier JSON** : Il est actuellement impossible d'écrire directement dans le fichier JSON depuis l'application. Si vous avez besoin de sauvegarder les modifications de manière permanente, vous devez mettre à jour manuellement le fichier JSON.
- **Stockage volatile des données** : Le fichier JSON sert de stockage temporaire. Toutes les modifications effectuées dans l'application sont stockées en RAM et seront perdues lors du redémarrage du serveur.

---

## **Contribuer**

Actuellement, ce projet n'accepte pas les contributions externes. Cependant, n'hésitez pas à forker le dépôt et à effectuer vos propres modifications.

---

## **Tests**

Aucun test unitaire n'a été défini pour ce projet pour le moment. Les contributions dans ce domaine sont les bienvenues !

---

## **Licences**

Aucune licence officielle n'a été définie pour ce projet. Pour les licences respectives des technologies utilisées, veuillez consulter leur documentation officielle :

- **VueJS** : [VueJS License](https://vuejs.org/)
- **FastAPI** : [FastAPI License](https://fastapi.tiangolo.com/)
- **Uvicorn** : [Uvicorn License](https://www.uvicorn.org/)

---

## **Technologies utilisées**

- **VueJS** : Un framework JavaScript pour construire des interfaces utilisateurs.
- **Axios** : Une bibliothèque pour effectuer des requêtes HTTP, utilisée dans le front-end pour interagir avec le back-end.
- **FastAPI** : Un framework Python pour construire des API rapides et modernes.
- **Uvicorn** : Un serveur ASGI pour exécuter l'application FastAPI.

---

## **Auteurs**

- **Geoffrey Valade** – Créateur et développeur principal du projet.

---

## **Note**

Si vous souhaitez en savoir plus sur les versions spécifiques de **VueJS**, **FastAPI** ou **Uvicorn** utilisées dans le projet, vous pouvez consulter les fichiers de configuration suivants :

- **`package.json`** pour les versions de **VueJS** et **Axios**.
- **`requirements.txt`** pour les versions de **FastAPI** et **Uvicorn**.
