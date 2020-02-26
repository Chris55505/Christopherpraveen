# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
pipe_lr = Pipeline([('scl', StandardScaler()),('pca', 
                  PCA(n_components=4)),('slr', LinearRegression())])


df=pd.read_csv("cruise_ship_info.csv")
cols_selected = ['Tonnage', 'passengers', 'length', 'cabins','crew']

X = df[cols_selected].iloc[:,0:4].values 
    
y = df[cols_selected]['crew'] 


sc_y = StandardScaler()
train_score = []
test_score =  []
