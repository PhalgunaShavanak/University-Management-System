import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import nltk

# Example ML model setup (adapt according to your needs)
def train_model():
    # Example dataset loading
    data = pd.read_csv('data.csv')  # Load your data
    X = data['text']
    y = data['label']
    
    # Create a pipeline that combines a CountVectorizer and a RandomForestClassifier
    model = make_pipeline(CountVectorizer(), RandomForestClassifier())
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model.fit(X_train, y_train)
    
    predictions = model.predict(X_test)
    print(f'Accuracy: {accuracy_score(y_test, predictions)}')
    return model

# Example function to predict
def predict(text, model):
    return model.predict([text])[0]
