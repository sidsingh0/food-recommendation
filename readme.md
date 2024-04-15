
# Recipe Labs

Recipe Labs, is a smart recipe recommendation application. It helps users figure out what food they can make with the ingredients they have and also recommend similar recipes based on properties of the food.

To view developer guide click [here](https://github.com/sidsingh0/food-recommendation/blob/master/dev.md).

## Index

- [Features](#features)
- [Setting up the app](#run-locally)
    - [Running with Docker](#running-with-docker)
    - [Running with Docker](#running-without-docker)
- [Usage](#usage)

## Features

- Recommend recipes based on the input.
- Recommend similar dishes based on a dish.
- Wishlist to save recipes.


## Run Locally

To run the project locally, there are 2 methods, with docker and without docker.

### Running with docker

To run the project with docker, make sure you have [Docker](https://docs.docker.com/get-docker/) and [Git](https://git-scm.com/downloads) installed on your system. 

Step 1: Clone the project

```bash
  git clone https://github.com/sidsingh0/food-recommendation.git
```

Step 2: Navigate to food-recommendation directory

```bash
  cd food-recommendation
```

Step 3: Start the project using docker compose

```bash
  docker-compose up --build
```

Step 5: To access the application, go to your browser and type `http://localhost:8080` in the address bar.

Step 6: Exit the application.

```bash
  docker-compose down
```

### Running without docker

Make sure you have installed [Node](https://nodejs.org/en/download), [Python](https://www.python.org/downloads/), [MongoDB](https://www.mongodb.com/try/download/community) and [Git](https://git-scm.com/downloads) on your system.
Also make sure your MongoDB service is running.

Step 1: Clone the project

```bash
  git clone https://github.com/sidsingh0/food-recommendation.git
```

Step 2: Navigate to food-recommendation/backend directory

```bash
  cd food-recommendation/backend
```

Step 3: Install the python dependencies

```bash
  pip install -r requirements.txt
```

Step 4: Open models/user_model.py in a text editor and change `self.client=MongoClient("mongodb://mongodb:27017")` to your local MongoDB URI.

Step 5: While in backend directory, start the backend service.

```bash
  waitress-serve --listen=*:5000 app:app
```

Step 6: Open a new terminal and navigate to frontend directory

```bash
  cd food-recommendation/frontend
```

Step 7: Install the required packages using npm

```bash
  npm install
```

Step 8: Build the application

```bash
  npm run build
```

Step 9: Run the application

```bash
  npm run preview
```

Step 10: To access the application, go to your browser and type `http://localhost:8080` in the address bar.

## Usage

Step 1: Open a browser and type `localhost:8080` in the Address bar.

![home](https://raw.githubusercontent.com/sidsingh0/food-recommendation/master/screenshots/home.png)

Step 2: Click on the Signin Button at the top right, and either sign in, or create a new account.

![signin](https://raw.githubusercontent.com/sidsingh0/food-recommendation/master/screenshots/signin.png)

Step 3: Click on the explore button. Enter the ingredients and time you can spare for cooking (in minutes).  

![questions](https://raw.githubusercontent.com/sidsingh0/food-recommendation/master/screenshots/questions.png)

Step 4:  You will get a list of recipes that match your requirements. You will also get similar recipes that require a few ingredients more. You can click on the dish to go to the recipe page or you can wishlist the recipe for later.

![results](https://raw.githubusercontent.com/sidsingh0/food-recommendation/master/screenshots/results.png)

Step 5: Once you click on the dish, you will get all the details about the dish, nutrition and a list of similar dishes too!

![dish](https://raw.githubusercontent.com/sidsingh0/food-recommendation/master/screenshots/dish.png)

Step 6: You can also use the checklist to follow while cooking.

![checklist](https://raw.githubusercontent.com/sidsingh0/food-recommendation/master/screenshots/checklist.png)

Step 7: Press on the Wishlist tab, to see your saved dishes and get recommendations based on it.

![wishlist](https://raw.githubusercontent.com/sidsingh0/food-recommendation/master/screenshots/wishlist.png)

