import pandas as pd
import numpy as np
import time
import re
import json

#Spacy
import spacy
nlp = spacy.load('en_core_web_sm')
#NLTK
import nltk
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import CleanData as clean

class AspectsAnalysis():
    def get_nouns_tag(newText, aspect_list):
        tagged = nltk.pos_tag(newText)
        for (word, tag) in tagged:
            if tag in ['NN']:  # If the word is a proper noun
                aspect_list.append(word)

    # remove all pronouns
    def get_nouns_pos(text):
        for t in text:
            if (t.pos_ == "NOUN"):
                return text

        return ""

    def get_nouns_setiment(nouns_list, data):
        sen = []
        tex = []
        for i in nouns_list:
            pos = 0
            neg = 0
            for j in range(len(data)):
                if i in data.loc[j]['review']:
                    tex.append(i)
                    sen.append(data.loc[j]['sentiment'])
        return tex, sen

    def get_aspects(self, data):
        data = data['review']
        tf_idf = Counter(" ".join(data).split()).most_common(400)
        dic = dict(tf_idf)
        llist = []
        self.get_nouns_tag(dic.keys(), llist)
        llist = [nlp(llist[t]) for t in range(len(llist))]
        aspect_list = [self.get_nouns_pos(t) for t in llist]
        aspect_list = [str(aspect_list[t][0]) for t in range(len(aspect_list)) if
                       aspect_list[t] != [] and aspect_list[t] != ""]
        new_dic = {}
        for i in range(len(aspect_list)):
            new_dic[aspect_list[i]] = dic.get(aspect_list[i])
        new_dic = {k: v for k, v in new_dic.items() if v is not None}
        noun, sentiment = self.get_nouns_setiment(list(new_dic.keys())[:8], data)
        dataSentiment = pd.DataFrame({'word': noun, 'sentiment': sentiment})
        sentimentCount = dataSentiment.value_counts()
        js = sentimentCount.to_json(orient='records')
        dataJson = json.loads(js)
        freq = nltk.FreqDist(sentimentCount.index)
        d = pd.DataFrame({'word': list(freq.keys()), 'Count': dataJson})
        json_data = d.to_json(orient='records')
        return json_data


