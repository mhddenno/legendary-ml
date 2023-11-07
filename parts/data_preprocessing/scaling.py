#!/usr/bin/env python

import pandas as ps
from sklearn.preprocessing import MinMaxScaler

data = pd.DataFrame({
    "people": ['A', 'B', 'C'], 
    "salary": [70000,60000,52000], 
    "age": [45,44,40]
})

## Normalization
c_1 = data[1]-data.min()[0]/data.max()[0]-data.min()[0]
c_2 = data[2]-data.min()[1]/data.max()[1]-data.min()[1]

result = pd.DataFrame({
    "people": ['A', 'B', 'C'], 
    "salary": c_1, 
    "age": c_2
})

## OR

## Using function
def normalize_column(column):
    min_val = column.min()
    max_val = column.max()
    normalized_column = (column - min_val) / (max_val - min_val)
    return normalized_column

df["salary"] = normalize_column(df["salary"])
df["age"] = normalize_column(df["age"])

## OR

# Initialize MinMaxScaler
scaler = MinMaxScaler()

# Normalize the "Salary" and "Age" columns
df[["Salary", "Age"]] = scaler.fit_transform(df[["Salary", "Age"]])


## Standardization