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
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
# import joblib
from joblib import dump


from sklearn import metrics
from sklearn.metrics import classification_report

df = pd.read_csv('amazonReview.csv')
df = df[['Review body', 'sentiment']]
df.columns = ['review', 'sentiment']
df['review'] = df['review'].astype('U')

print(df.head())
print(df.sentiment.value_counts())

df2 = pd.read_csv('Amazon_Mobile.csv')
df2 = df2[['Reviews', 'Rating']]
df2.columns = ['review', 'sentiment']
mapping = {1:'negative', 2:'negative', 3:'negative', 4:'positive', 5:'positive'}
df2['sentiment'] = df2['sentiment'].map(mapping)
df2['review'] = df2['review'].astype('U')

print(df2.head())
print(df2.sentiment.value_counts())

df = df.append(df2)
print(df.sentiment.value_counts())

def remove_urls(text):
    url_pattern = re.compile(r'https?://\S+|www\.\S+|@[^\s]+')
    cleantext = url_pattern.sub(r'', text)
    return cleantext

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  cleantext = re.sub(' +', ' ', cleantext)
  return cleantext

df["review"] = df["review"].map(remove_urls)
df["review"] = df["review"].map(cleanhtml)

print(df.head())

# Create series to store the features and labels
y = df.sentiment
x = df.review

# Initialize a CountVectorizer object: count_vectorizer
count_vectorizer = CountVectorizer(stop_words = 'english')

# Transform the training data using only the 'text' column values: count_train
count_train = count_vectorizer.fit_transform(x)

rf_clf = RandomForestClassifier()

# Fit the classifier to the training data
rf_clf.fit(count_train, y)

# define the stages of the pipeline
pipeline = Pipeline(steps= [('CountVectorizer', CountVectorizer(stop_words = 'english')),
                            ('model', RandomForestClassifier())])

# fit the pipeline model with the training data
pipeline.fit(x, y)

# dump the pipeline model
dump(pipeline, filename="visionalyst_classifier_rf.joblib")