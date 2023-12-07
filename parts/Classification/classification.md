**<h3> Classification models </h3>**
<h4> Unlike regression where you predict a continuous number, you use classification to predict a category. 
</h4>

**<h3> Logistic Regression </h3>**

<h4>  

-   Logistic Regression is a linear classifier. 
-   Despite its name, logistic - regression is used for binary classification problems, where the output is a binary variable (e.g., 0 or 1, true or false).

-   The logistic regression algorithm applies a linear transformation to the input features
-   Then passes the result through a logistic (sigmoid) function to obtain the final output. 
-   Logistic regression applies the logistic function to produce values between 0 and 1, representing probabilities.

- $$  P(Y=1) = \frac{1}{1 + e^{-(b_0 + b_1x_1 + b_2x_2 + \ldots + b_nx_n)}}  $$

where:
- $ P(Y=1) $ is the probability of the event (Y) being class 1, 
- $ (e) $ is the base of the natural logarithm,
- $ (b_0, b_1, b_2, \ldots, b_n) $ are the coefficients,
- $ (x_1, x_2, \ldots, x_n) $ are the input features.

</h4>

**<h3> K-Nearest Neighbors (K-NN) </h3>**
<h4>  



</h4>

**<h3> Support Vector Machine (SVM) </h3>**
<h4>


</h3>

**<h3> Kernel SVM </h3>**
<h3>



</h3>

**<h3> Naive Bayes </h3>**

<h4>

-   Naive Bayes describes the probability of an event based on prior knowledge of conditions that might be related to the event. (and that's why it is called Naive ==> we are assuming, we don't know!)
-   The Naive comes from the assumption that features used to describe an observation are conditionally independent! given that class label. This is a simplifying assumption that makes algorithm computationally effcient.
-   The assumption of feature independence simplifies the computation of probabilites. Even though theis assumption might not hold in reality, NB ofgen performs surprisingly well in practice.
-   There are many varients of Naive Bayes (Multinomial NB commonly used for text classification), (Gaussian NB suitable for continuous data assuming the Gaussian distribution)
-   NB is computationally efficient and scales well with the number of features. It requires a relatively small amout of training data to estimate the necessary parameters.
-   NB is a powerful and simple algorithm, it may not perform well in situations where the independence assumption is strongly violated or when interactions between features significantly impact the outcome.
-   Practical example [here](./naive_bayes.md)

</h4>

**<h3> Decision Tree Classification </h3>**
<h3>


</h3>

**<h3> Random Forest Classification </h3>**
<h3>


</h3>

**<h3> Comparison </h3>**

