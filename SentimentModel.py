import pandas as pd
import numpy as np
import time
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.pipeline import Pipeline
import joblib
from joblib import dump
from joblib import load

class SentimentModel():
    def get_sentiment(df):
        # load the saved pipleine model
        pipeline = load("visionalyst_classifier_dt.joblib")

        # predict on the sample tweet text
        prediction = pipeline.predict(df['review'])

        df['sentiment'] = prediction

        return df