#!/usr/bin/env python

import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler

data = pd.DataFrame({
    "people": ['A', 'B', 'C'], 
    "salary": [70000,60000,52000], 
    "age": [45,44,40]
})

print(data)

#     people  salary  age
#   0      A   70000   45
#   1      B   60000   44
#   2      C   52000   40

## Normalization
c_1 = (data.iloc[:,1]-data.iloc[:,1].min())/(data.iloc[:,1].max()-data.iloc[:,1].min())
c_2 = (data.iloc[:,2]-data.iloc[:,2].min())/(data.iloc[:,2].max()-data.iloc[:,2].min())

result = pd.DataFrame({
    "people": ['A', 'B', 'C'], 
    "salary": c_1, 
    "age": c_2
})

print(result)

## OR

## Using function
result=data
def normalize_column(column):
    min_val = column.min()
    max_val = column.max()
    normalized_column = (column - min_val) / (max_val - min_val)
    return normalized_column

result["salary"] = normalize_column(data["salary"])
result["age"] = normalize_column(data["age"])


print(result)

## OR

# Initialize MinMaxScaler
result=data
scaler = MinMaxScaler()

# Normalize the "Salary" and "Age" columns
result[["salary", "age"]] = scaler.fit_transform(data[["salary", "age"]])
print(result)

# All results 
#     people    salary  age
#   0      A  1.000000  1.0
#   1      B  0.444444  0.8
#   2      C  0.000000  0.0

## Standardization

result=data
# Initialize StandardScaler
scaler = StandardScaler()

# Fit and transform the DataFrame
result = pd.DataFrame(scaler.fit_transform(data[['salary', 'age']]))

print(result)

# OR

result=data
# Standardize the DataFrame using pandas
result = (result[['salary', 'age']] - result[['salary', 'age']].mean()) / result[['salary', 'age']].std()

print(result)
