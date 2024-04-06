import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import StandardScaler
from scipy.sparse import hstack

class Recommender():
    
    def __init__(self):
        with open('data/model.pkl', 'rb') as file:
            self.model = pickle.load(file)
        self.df=pd.read_csv('data/dishes.csv')
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.description_vec = self.vectorizer.fit_transform(self.df['description'])
        self.ingredients_vec = self.vectorizer.fit_transform(self.df['ingredients'])
        self.tags_vec = self.vectorizer.fit_transform(self.df['tags'])
        self.name_vec = self.vectorizer.fit_transform(self.df['name'])
        self.scaler = StandardScaler()
        self.numerical_features = self.df[['calories', 'total_fat', 'sugar', 'sodium', 'protein', 'saturated_fat', 'carbohydrates']]
        self.numerical_features_scaled = self.scaler.fit_transform(self.numerical_features)
    
    def recommend(self,id):
        input_combined_features =  hstack([self.description_vec[id] * 0.1, self.tags_vec[id] * 0.1, self.name_vec[id] * 0.15, self.ingredients_vec[id] * 0.4, self.numerical_features_scaled[id].reshape(1, -1) * 0.35])
        nearest_dishes_distances, nearest_dishes_indices = self.model.kneighbors(input_combined_features)
        return (nearest_dishes_indices)

recommender=Recommender()
print(recommender.recommend(2))