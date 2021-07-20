import pandas as pd
import numpy as np
import time
import re
#Twitter
import tweepy
#Spacy
import spacy
#nlp = spacy.load('en_core_web_sm')
#NLTK
import nltk
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
#Charts
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from wordcloud import WordCloud, STOPWORDS
#Models
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
# import joblib
from joblib import dump
from joblib import load


# sample tweet text
text = ["Charger is not working", "I loved this product", 'I hated this product', "Good Product"]

# load the saved pipleine model
pipeline = load("visionalyst_classifier_rf.joblib")

df = pd.read_csv('Amazon_Mobile.csv')
df = df[:100]

# predict on the sample tweet text
prediction = pipeline.predict(df['Reviews'])

df['sentiment'] = prediction

print(df.columns)
print(df)