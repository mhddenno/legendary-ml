**<h3> Regression models (both linear and non-linear) </h3>**
<h4> Regression models (both linear and non-linear) are used for predicting a real value, like salary for example. If your independent variable is time, then you are forecasting future values, otherwise your model is predicting present but unknown values. Regression technique vary from Linear Regression to SVR and Random Forests Regression.
</h4>

**<h3> Simple Linear Regression </h3>**
<h4>  

- For example [click here](./linear_regression.ipynb)

</h4>

**<h3> Multiple Linear Regression </h3>**
<h4>  

- Scaling is not important because the *b0,b1, b3 ...* constants will play a compensation role in the equation.
- We don't need to check for the linearity conditions because if there is a linear relationship in the data then the accuracy will be top, if not the accuracy will be bad. Why to bother and test that?
- We don't need to get rid of the dummy variables (dummy variable trap) after encoding because the *regressor* will do that for us.
- Do we have to choose the best features (features with highest p-values) using the algorithms [here](../data_preprocessing/building_model.md) No! because the *regressor* will do that alone. In another words Backward Elimination is irrelevant in Python, because the Scikit-Learn library automatically takes care of selecting the statistically significant features when training the model to make accurate predictions. But for the sake of learning manuell Backward Elimination looks like this [click here](../statistics/backward_elimination.ipynb)
- For example [click here](./multiple_linear_regression.ipynb)

</h4>

**<h3> Polynomial Regression </h3>**
<h3>  </h3>

**<h3> Support Vector for Regression (SVR) </h3>**
<h3>  </h3>

**<h3> Decision Tree Regression </h3>**
<h3>  </h3>

**<h3> Random Forest Regression </h3>**
<h3>  </h3>