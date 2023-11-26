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

- The same concept of a linear regression line but it is a tube (epsilon insensitive tube) all points in the tube are excluded from the error calculations in other words it uses a loss function that penalizes deviations from the regression hyperplane. The loss function includes a term for both the deviation and the margin violations.
- It can be used for both classification and regression tasks.
- SVM is less sensitive to outliers due to the use of a margin-based loss function.
- SVM aims to find a hyperplane that best fits the data points in a higher-dimensional space.
- SVM model aims to find a hyperplane that maximizes the margin between different classes or fits the data points in the case of regression. 
- SVM can use different types of kernels to capture non-linear relationships For more [click here](./svm.md).
- For example [click here](./svm_regression.ipynb).

</h3>

**<h3> Decision Tree Regression </h3>**
<h3>

- A tree built structure with leafs and nodes, built recursively splitting data into subsets based on the values of input features.
- Terminal leafs represent the final output.
- The decision on how to split the data at each node is based on a splitting criterion.
- Common splitting criteria include mean squared error for regression tasks, which measures the variance of the target variable within each node.
- The process of creating the tree involves recursively splitting the data into subsets until a stopping condition is met.
- Stopping conditions may include a maximum tree depth, a minimum number of samples in a leaf node, or a minimum improvement in the splitting criterion.
- RT are robust against outliers because the spliting happens based on ranks rather values.
- RT can be prone to overfitting, capturing noise in the training data, Techniques like pruning or using ensemble methods can help metigate this issue.
- For example [click here](./regression_decision_tree.ipynb)
- [DT](../../res/DT.pdf)

</h3>

**<h3> Random Forest Regression (Ensemble Learning) </h3>**
<h3>

- Random Forest is an ensemble of decision trees, where multiple trees are built and combined to improve the overall predictive performance.
- The algorithm creates multiple random subsets of the training data (with replacement) to train individual decision trees Bagging (Bootstrap Aggregating).
- Random Feature Selection: At each node of the decision tree, a random subset of features is considered for splitting. This helps to decorrelate the trees and reduce overfitting.
- Tree Independence Each tree is constructed independently of the others, which enhances the diversity of the forest and prevents the model from being overly sensitive to specific patterns in the data.
- Voting or Averaging For classification tasks, the final prediction is determined by a majority vote from all the individual trees. For regression tasks, the final prediction is the average of predictions from all trees.
- Robust to Overfitting The combination of multiple trees and random feature selection makes Random Forest robust to overfitting, even on noisy datasets.
- High Predictive Accuracy Random Forest tends to have high predictive accuracy and performs well on a wide range of tasks without requiring extensive hyperparameter tuning.
- Feature Importance Random Forest provides a measure of feature importance, indicating the contribution of each feature to the overall predictive performance of the model.
- Parallelization Training individual trees in the forest can be done in parallel, making Random Forest efficient for large datasets.
- Hyperparameters Important hyperparameters include the number of trees in the forest, the maximum depth of each tree, and the number of features considered at each split.
- For example [click here](./random_forest.ipynb)

</h3>

**<h3> Comparison </h3>**

| Regression Model | Pros | Cons |
| :---------------: | :---------------: | :---------------: |
| Linear Regression    | Works on any size of dataset, gives informations about relevance of features | The Linear Regression Assumptions |
| Ploynomial Regression    | Works on any size of dataset, works very well on non linear problems | Need to choose the right polynomial degree for a good bias/variance tradeoff |
| SVR    | Easily adaptable, works very well on non linear problems, not biased by outliers | Compulsory to apply feature scaling, not well known, more difficult to understand  |
| Decision Tree    | Interpretability, no need for feature scaling, works on both linear / nonlinear problems | Poor results on too small datasets, overfitting can easily occur |
| Random Forest Regression    | Powerful and accurate, good performance on many problems, including non linear   | No interpretability, overfitting can easily occur, need to choose the number of trees |