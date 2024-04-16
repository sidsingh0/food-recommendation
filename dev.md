
# Recipe Labs - Developer Guide

This guide is meant for developers. To view the production guide and usage click [here](https://github.com/sidsingh0/food-recommendation/blob/master/readme.md).

## Index

- [Maching Learning](#machine-learning)
- [Frontend](#frontend)
- [Backend](#backend)
- [Database](#database)
- [Running locally in Dev mode](#running-locally)

## Maching Learning

The application comprises of 2 models, both of them use Nearest Neighbours algorithm. 

- The first model, is used for recommending similar dishes based on the features of current dish.
- The second model, is used together with filteration while searching for recipes based on ingredients and time.

The models are trained on Food.com dataset with over 200,000 data points, which can be accessed on [Kaggle](https://www.kaggle.com/datasets/shuyangli94/food-com-recipes-and-user-interactions).

To access the python notebook, click [here](https://github.com/sidsingh0/food-recommendation/blob/master/notebook/FoodRecommendation.ipynb).

## Frontend 

ReactJs is used for creating the frontend of the application for the following reasons

- Reusable components: The UI can be broken down into smaller, maintanable and reusable parts. Each React component can have its own internal state. This makes it easier to manage the data specific to that component's functionality and keeps the state organized.
- Good performance: Diffing makes ReactJs fast and only updates necessary parts in the actual DOM from the Virtual DOM.

The frontend code is organized in the following fashion:

- Components: This directory contains all the components that are used.
- Screens: Screens directory contains all the screens/pages of the website. These screens make use of components to create a larger organized UI.
- Services: This folder contains the logic for API calls and authentication.
  - ApiUrls contains all the mappings of apis.
  - ApiService contains the logic for making API calls, setting headers (Bearer token).
  - AuthContext and ProtectedRoute contain authentication logic. AuthContext uses react's context api for global login state accesibility. It also handles logout and logins.

![frontend](https://raw.githubusercontent.com/sidsingh0/food-recommendation/master/screenshots/frontendflow.png)

## Backend

Flask is used for creating the backend service for the following reasons:

- Lightweight: Flask is Lightweight and doesn't have extra dependencies. It suits our project's scale.
- Simple:  Due to its simplicity and ease of use, Flask is ideal for quickly building endpoints.

The backend code is organized in the following fashion:

- `app.py` - It contains the initializations for bcrypt, jwt and setting CORS.
- Data: This directory contains the pickle files and the database in CSV format. This is utilised by the dish_model for making recommendations.
- Controllers: Controllers contain the route to backend logic mapping. `dish_controller.py` contains mappings for urls related to dishes and `user_controller.py` contains mappings for urls related to the user.
- Models: Models have objects that encapsulate the logic for backend. `__init__` methods load the pre-requisites. 
  - `dish_model.py` utilises machine learning models (in .pkl format) as well as the dishes dataset to make predictions and get dish data.
  - `user_model.py` utilises the connection to mongodb database for storing and acccessing user data.
- Validators: They contain objects that utilise [PyDantic](https://github.com/pydantic/pydantic) for type checking, type enforcement and type validation for the User Model.

![backend](https://raw.githubusercontent.com/sidsingh0/food-recommendation/master/screenshots/backendflow.png)

## Database

MongoDB is used as the database for the following reasons:
- Easy to use and flexible schema.
- MongoDB can scale horizontally. It can store the data across various machines if necessary.

## Run locally in dev mode

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
  flask run
```

Step 6: Open a new terminal and navigate to frontend directory

```bash
  cd food-recommendation/frontend
```

Step 7: Install the required packages using npm

```bash
  npm install
```

Step 8: Open `vite.config.js` in a text editor and comment/remove the following line

```bash
  origin: "http://0.0.0.0:8080",
```

Step 9: Run the application

```bash
  npm run dev
```

Step 10: To access the application, go to your browser and type `http://localhost:8080` in the address bar. The backend api service is accesible at `http://localhost:5000`.

