#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[7]:


df = pd.read_csv("https://raw.githubusercontent.com/PacktPublishing/Python-Data-Analysis-Third-Edition/master/Chapter11/diabetes.csv")


# In[8]:


feature_set = ['pregnant', 'insulin', 'bmi','age','glucose','bp','pedigree']

features = df[feature_set]
target = df.label


# In[10]:


# partition data into training and testing set
from sklearn.model_selection import train_test_split
feature_train, feature_test, target_train, target_test = train_test_split(features, target, test_size=0.3, random_state=1)


# In[11]:


# Import K-means Clustering
from sklearn.cluster import KMeans
from sklearn.metrics import fowlkes_mallows_score

# Specify the number of clusters
num_clusters = 2

# Create and fit the KMeans model
km = KMeans(n_clusters=num_clusters)
km.fit(feature_train)

# Predict the target variable
predictions = km.predict(feature_test)

# Calculate internal performance evaluation measures
print("Fowlkes Mallows Score:", fowlkes_mallows_score(target_test,
predictions))

