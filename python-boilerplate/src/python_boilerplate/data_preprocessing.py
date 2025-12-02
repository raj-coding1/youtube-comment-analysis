import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

#data preprocessing function
def preprocess_data(comment):

    #lowering the comment
    comment = comment.lower()

    #stripping the comment
    comment = comment.strip()

    #removal of new line character
    comment = re.sub('\n','',comment)

    #removal of special character
    comment = re.sub(r'[^A-Za-z0-9\s!?.]','', comment)

    #removal of stopwords
    stop_words = set(stopwords.words('english')) - {'no','not','but'}
    comment = ' '.join([word for word in comment.split() if word not in stop_words])

    #lemmatizing of words
    lemmatizer = WordNetLemmatizer()
    comment = ' '.join([lemmatizer.lemmatize(word) for word in comment.split()])

    return comment

df['clean_comment'] = df['clean_comment'].apply(preprocess_data)
