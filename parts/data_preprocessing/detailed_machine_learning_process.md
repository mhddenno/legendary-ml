<h3>  Importing the necessary libraries </h3> 

```
import pandas as pd # data manipulation
import numpy as np # numerical operations
from sklearn.model_selection import train_test_split # for spliting
from sklearn.impute import SimpleImputer # for missing data
```

<h3> Loading the Iris dataset </h3> 

```
dataset = pd.read_csv("iris.csv") 
```

<h3> Creating the matrix of features (X) and the dependent  variable vector (y) </h3> 

```
X = dataset.iloc[:,:-1].values #features
y = dataset.iloc[:,-1].values #dependent variables 
# PS .values attribute to extract the data as numpy arrays.
```

<h3> Taking care of missing </h3> 

<h4> Load the dataset </h4>

```
dataset = pd.read_csv("pima-indians-diabetes.csv")
```

<h4> Identify missing data (assumes that missing data is represented as NaN) </h4>

```
missing_data = dataset.isnull().sum()
```

<h4> Configure an instance of the SimpleImputer class </h4>

```
imputer = SimpleImputer(missing_values=np.nan, strategy = "mean")
```

<h4> Fit the imputer on the DataFrame </h4>

```
imputer.fit(dataset.iloc[:,0:9])
```

<h4> Apply the transform to the DataFrame </h4>

```
dataset.iloc[:,0:9]=imputer.transform(dataset.iloc[:,0:9])
```
<h3> Encoding categorical data </h3> 

<h4> Encoding the Independent/Dependent Variable </h4> 

[see here](./data_preprocessing/encoding.ipynb)

<h3> Spliting </h3> 

[see here](./data_preprocessing/spliting.ipynb)

<h3> Sclaing </h3> 

[see here](./data_preprocessing/scaling.ipynb)
