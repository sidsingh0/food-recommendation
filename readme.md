# Recipe Labs

Recipe Labs, is a smart recipe recommendation application. It helps users figure out what food they can make with the ingredients they have and also recommend similar recipes based on properties of the food.

The models are trained on Food.com dataset, which can be accessed on [Kaggle](https://www.kaggle.com/datasets/shuyangli94/food-com-recipes-and-user-interactions). 


To view the model building and data pre-processing steps, you can visit [here](https://github.com/sidsingh0/food-recommendation/blob/master/notebook/FoodRecommendation.ipynb)


## Index

- [Introduction](#introduction)
- [Features](#features)
- [Technologies](#technologies)
- [Setting up the app](#setting-up-the-app)
- [Usage](#usage)

## Features

- Feature 1: Recommend recipes based on the input.
- Feature 2: Recommend similar dishes based on a dish.
- Feature 3: Wishlist to save recipes.

## Technologies

The app primarily, utilises Flask for backend to make it lightweight with minimal dependencies. React is used for frontend. The frontend, backend and the database is containerized using Docker.

- Languages: Python, Javascript, HTML, CSS
- Backend: Flask
- Frontend: ReactJS
- Database: MongoDB

## Setting up the app

### With Docker

Make sure you have [Docker](https://docs.docker.com/get-docker/) and [Git](https://git-scm.com/downloads) installed on your system. 

Run the following commands to use the app using Docker:

1. Clone the repository

```
git clone https://github.com/sidsingh0/food-recommendation.git
```

2. Navigate to food-recommendation folder

```
cd food-recommendation
```

3. Start the project using docker compose

```
docker-compose up --build
```

4. Use the application

To access the application, go to your browser and type `http://localhost:8080` in the url. 

5. Exit the application.

To stop the application write this command in terminal. 

```
docker-compose stop
```

OR

To stop the application and remove all the created containers, write this command in terminal.

```
docker-compose down
```

### Without Docker

Make sure you have installed [Node](https://nodejs.org/en/download), [Python](https://www.python.org/downloads/), [MongoDB](https://www.mongodb.com/try/download/community) and [Git](https://git-scm.com/downloads) on your system.

Make sure your MongoDB service is running.

1. Clone the repository

```
git clone https://github.com/sidsingh0/food-recommendation.git
```

2. Open a terminal and write 

```
cd food-recommendation/backend
```

3. Install the required packages

```
pip install -r requirements.txt
```

4. Open models directory

```
cd models
```

with your own MongoDB URI

5. Open user_model.py in a text editor and replace

```
self.client=MongoClient("mongodb://mongodb:27017")
```

with your own MongoDB URI


6. Navigate back to backend folder and start the backend service

```
cd ..
waitress-serve --listen=*:5000 app:app
```

7. Open a new terminal and navigate to frontend directory

```
cd food-recommendation/frontend
```

8. Install the required packages using

```
npm i
```

9. Build the application using

```
npm run build
```

10. Run the application using

```
npm run start
```

11. Use the application

To access the application, go to your browser and type `http://localhost:8080` in the url. 

## Usage

1. Open a browser and type `localhost:8080` in the Address bar.
![home](https://raw.githubusercontent.com/sidsingh0/food-recommendation/master/screenshots/home.png)

2. Click on the Signin Button at the top right, and either sign in, or create a new account.
![signin](https://raw.githubusercontent.com/sidsingh0/food-recommendation/master/screenshots/signin.png)

3. Click on the explore button. Enter the ingredients and Time you can spare for cooking (in minutes).  
![questions](https://raw.githubusercontent.com/sidsingh0/food-recommendation/master/screenshots/questions.png)

4. You will get a list of recipes that match your requirements. You will also get similar recipes that require a few ingredients more. You can click on the dish to go to the recipe page or you can wishlist the recipe for later.
![results](https://raw.githubusercontent.com/sidsingh0/food-recommendation/master/screenshots/results.png)

5. Once you click on the dish, you will get all the details about the dish, nutrition and a list of similar dishes too!
![dish](https://raw.githubusercontent.com/sidsingh0/food-recommendation/master/screenshots/dish.png)

6. You can also use the checklist to follow while cooking.
![checklist](https://raw.githubusercontent.com/sidsingh0/food-recommendation/master/screenshots/checklist.png)

7. Press on the Wishlist tab, to see your saved dishes and get recommendations based on it.
![wishlist](https://raw.githubusercontent.com/sidsingh0/food-recommendation/master/screenshots/wishlist.png)





