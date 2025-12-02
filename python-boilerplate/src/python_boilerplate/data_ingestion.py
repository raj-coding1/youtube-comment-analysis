import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
import os
import yaml

#load the parameter
curr_dir = os.path.dirname(os.path.abspath(__file__))
print(curr_dir)
params_path = os.path.join(curr_dir, '..','..','params.yaml')

with open(os.path.realpath(params_path), 'r') as file:
    params = yaml.safe_load(file)

#load the data
df = pd.read_csv('https://raw.githubusercontent.com/Himanshu-1703/reddit-sentiment-analysis/refs/heads/main/data/reddit.csv')

#remove missing value
df.dropna(axis = 0,inplace = True)

#drop duplicate values
df.drop_duplicates(inplace = True)

#remove blank values
df = df[~(df['clean_comment'].str.strip() == '')]

# #divide the data into X and y
# X = df['clean_comment']
# y = df['category']

#split the data
train_data, test_data = train_test_split(
    df, 
    test_size= params['data_ingestion']['test_size'],
    random_state=42
)
print(params)
path = os.path.realpath(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','data'))
os.makedirs(path,exist_ok = True)
paths = os.path.join(path,'train_data.csv')
print(path)
print(paths)
pathss = os.path.join(path,'test_data.csv')
train_data.to_csv(paths,index = False)
test_data.to_csv(pathss,index = False)




    