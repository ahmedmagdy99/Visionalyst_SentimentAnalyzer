import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import regex as re
from datetime import datetime

class CleanData():
    def remove_urls(text):
        url_pattern = re.compile(r'https?://\S+|www\.\S+|@[^\s]+')
        cleantext = url_pattern.sub(r'', text)
        return cleantext

    def clean_html(text):
        cleanr = re.compile('<.*?>')
        cleantext = re.sub(cleanr, '', text)
        cleantext = re.sub(' +', ' ', cleantext)
        return cleantext

    def clean_mentions_and_endline(text):
        cleanr = re.compile('\n|@[^\s]+')
        cleantext = re.sub(cleanr, '', text)
        return cleantext