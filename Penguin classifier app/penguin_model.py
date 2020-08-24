
import pandas as pd
import pickle

penguins = pd.read_csv('penguins_cleaned.csv')


df = penguins.copy()
target = 'species'
encode = ['sex','island']


for col in encode:
    dummy = pd.get_dummies(df[col],prefix = col)
    
