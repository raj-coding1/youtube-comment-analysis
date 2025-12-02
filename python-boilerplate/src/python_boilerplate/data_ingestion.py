import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

#load the data
df = pd.read_csv('https://raw.githubusercontent.com/Himanshu-1703/reddit-sentiment-analysis/refs/heads/main/data/reddit.csv')

#remove missing value
df.dropna(axis = 0,inplace = True)

#drop duplicate values
df.drop_duplicates(inplace = True)

#remove blank values
df = df[~(df['clean_comment'].str.strip() == '')]

#divide the data into X and y
X = df['clean_comment']
y = df['category']

#split the data
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)




    