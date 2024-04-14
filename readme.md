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

## Introduction

exercise.me is a fitness web app that is designed for users to help them in their exercise selection process. There are two ways in which the user can be recommended:

 - First way: To enter a specific input according to the need of the user. This can include, for example, 'exercises without equipment'. This input is then passed to the backend of the application and then 5 best exercises are recommended according to this input. (Login is required for this feature)

 - Second way: To select a specific muscle on the body figure provided in the application. The muscles which are available are: Arms, Legs, Core, Chest, Triceps, Glutes, Lower Back and Upper Back. The body can be mapped to add more muscles in future. The selected muscle is then sent to backend and again 5 best exercises are recommended.

Not only recommendation, but this app also contains a BMI (Body Mass Index) calculator which takes in height (in cms) and weight (in kgs) of the user and provide them with the appropriate BMI category.

## Features

- Feature 1: Recommend recipes based on the input.
- Feature 2: Recommend similar dishes based on a dish.
- Feature 3: Wishlist to save recipes

## Technologies

The app primarily, utilises Flask for backend to make it lightweight with minimal dependencies. React is used for frontend. The frontend, backend and the database is containerized using Docker.

- Languages: Python, Javascript, HTML, CSS
- Backend: Flask
- Frontend: ReactJS
- Database: MongoDB

## Setting up the app

### With Docker

Make sure you have [Docker](https://docs.docker.com/get-docker/) and (Git)[https://git-scm.com/downloads] installed on your system. 

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

Make sure you have installed [Node](https://nodejs.org/en/download), [Python](https://www.python.org/downloads/), [MongoDB](https://www.mongodb.com/try/download/community) and (Git)[https://git-scm.com/downloads] on your system.

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

4. Open models/user_model.py in a text editor and replace

```
self.client=MongoClient("mongodb://mongodb:27017")
```

with your own MongoDB URI


5. Navigate back to backend folder and start the backend service

```
waitress-serve --listen=*:5000 app:app
```

6. Open a new terminal and navigate to frontend directory

```
cd food-recommendation/frontend
```

7. Install the required packages using

```
npm i
```

8. Build the application using

```
npm run build
```

9. Run the application using

```
npm run start
```

10. Use the application

To access the application, go to your browser and type `http://localhost:8080` in the url. 
