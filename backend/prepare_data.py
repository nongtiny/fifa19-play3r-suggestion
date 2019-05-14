import pandas as pd
import numpy as np

import os

dataset = pd.read_csv("../input/data.csv")

query_data = dataset[['ID', 'Nationality', 'Age', 'Position', 'Height', 'Weight']]

def feet2cm(x):
    x = str(x).replace('\'','.')
    res = float(x) * 30.48
    return res

def lbs2kg(x):
    x = str(x)[0:3]
    res = float(x) / 2.205
    return res

def convert_currency(x):
    x = x.replace('€','')
    if x.endswith("M"):
        return float(x.split("M")[0]) * 1000000
    elif x.endswith("K"):
        return float(x.split("K")[0]) * 1000


#Feet to cm: multiply the length value by 30.48
query_data['Height'] = query_data['Height'].apply(lambda x: feet2cm(x))
#Pound to kg: divided by 2.205
query_data['Weight'] = query_data['Weight'].apply(lambda x: lbs2kg(x))
# Numeric value in Euros
dataset['Value'] = dataset['Value'].apply(convert_currency) 
dataset['Wage'] = dataset['Wage'].apply(convert_currency) 
dataset['Weight'] = dataset['Weight'].apply(lambda x: lbs2kg(x))
dataset['Height'] = dataset['Height'].apply(lambda x: feet2cm(x))

compute_similarity_data = dataset[['ID', 'Value', 'Overall', 'LS', 'ST', 'RS', 'LW', 'LF', 'CF', 'RF',
'LAM', 'CAM', 'RAM', 'LM', 'LCM', 'CM', 'RCM', 'RM', 'LWB', 'LDM', 'CDM',
'RDM', 'RWB', 'LB', 'LCB', 'CB', 'RCB', 'RB', 'Crossing', 'Finishing', 
'HeadingAccuracy', 'ShortPassing', 'Volleys', 'Dribbling', 'Curve', 
'FKAccuracy', 'LongPassing', 'BallControl', 'Acceleration', 'SprintSpeed',
'Agility', 'Reactions', 'Balance', 'ShotPower', 'Jumping', 'Stamina', 'Strength', 'LongShots'
, 'Aggression','Interceptions', 'Positioning', 'Vision', 'Penalties', 'Composure', 'Marking', 'StandingTackle', 'SlidingTackle'
, 'GKDiving', 'GKHandling', 'GKKicking', 'GKPositioning', 'GKReflexes']] 

query_data.to_csv("../input/query.csv")
compute_similarity_data.to_csv("../input/compute_similarity.csv")
dataset.to_csv("../input/use_this_dataset.csv")

props = ['Crossing', 'Finishing', 'HeadingAccuracy', 'ShortPassing', 'Volleys', 'Dribbling',
'Curve', 'FKAccuracy', 'LongPassing', 'BallControl', 'Acceleration', 'SprintSpeed',
'Agility']
positions = ['Overall','LS', 'ST', 'RS',
'LW', 'LF', 'CF', 'RF', 'LAM', 'CAM', 'RAM', 'LM', 'LCM', 'CM', 'RCM', 
'RM', 'LWB', 'LDM', 'CDM', 'RDM', 'RWB', 'LB', 'LCB', 'CB', 'RCB', 'RB']

d = dataset.Nationality.unique()
# print(sorted(d))