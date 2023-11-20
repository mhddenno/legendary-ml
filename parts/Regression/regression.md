**<h3> Regression models (both linear and non-linear) </h3>**
<h4> Regression models (both linear and non-linear) are used for predicting a real value, like salary for example. If your independent variable is time, then you are forecasting future values, otherwise your model is predicting present but unknown values. Regression technique vary from Linear Regression to SVR and Random Forests Regression.
</h4>

**<h3> Simple Linear Regression </h3>**
<h4>  

- $$ y = b_{0} + b_{1} * X  $$
- For example [click here](./linear_regression.ipynb)

</h4>

**<h3> Multiple Linear Regression </h3>**
<h4>  

- $$ y = b_{0} + b_{1} * X_{1} + b_{2} * X_{2} + b_{3} * X_{3} + ... + b_{n} * X_{n} $$
- Scaling is not important because the *b0,b1, b3 ...* constants will play a compensation role in the equation.
- We don't need to check for the linearity conditions because if there is a linear relationship in the data then the accuracy will be top, if not the accuracy will be bad. Why to bother and test that?
- We don't need to get rid of the dummy variables (dummy variable trap) after encoding because the *regressor* will do that for us.
- Do we have to choose the best features (features with highest p-values) using the algorithms [here](../data_preprocessing/building_model.md) No! because the *regressor* will do that alone. In another words Backward Elimination is irrelevant in Python, because the Scikit-Learn library automatically takes care of selecting the statistically significant features when training the model to make accurate predictions. But for the sake of learning manuell Backward Elimination looks like this [click here](../statistics/backward_elimination.ipynb)
- For example [click here](./multiple_linear_regression.ipynb)

</h4>

**<h3> Polynomial Regression </h3>**
<h4>

- $$ y = b_{0} + b_{1} * X + b_{2} * X^2 + b_{3} * X^3 + ... + b_{n} * X^n $$
- Attention the X is the same here ;)
- Fun fact The linearity in this context refers to the parameters of the model, not the shape of the curve
- For example [click here](./ploynomial_regression.ipynb)

</h4>

**<h3> Support Vector for Regression (SVR) </h3>**
<h3>

- The same concept of a linear regression line but it is a tube all points in the tube are excluded from the error calculations in other words it uses a loss function that penalizes deviations from the regression hyperplane. The loss function includes a term for both the deviation and the margin violations.
- It can be used for both classification and regression tasks.
- SVM is less sensitive to outliers due to the use of a margin-based loss function.
- SVM aims to find a hyperplane that best fits the data points in a higher-dimensional space.
- SVM model aims to find a hyperplane that maximizes the margin between different classes or fits the data points in the case of regression. 
- SVM can use different types of kernels to capture non-linear relationships For more [click here](./svm.md).
- For example [click here](./svm_regression.ipynb).

</h3>

**<h3> Decision Tree Regression </h3>**
<h3>  </h3>

**<h3> Random Forest Regression </h3>**
<h3>  </h3>