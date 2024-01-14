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

 -  first we choose k, the number of clusters we want to find in the data. Then, the centers of those k clusters, called centroids, are initialized in some fashion.

 -  The algorithm then proceeds in two alternating parts: In the Reassign Points step, we assign every point in the data to the cluster whose centroid is nearest to it. In the Update Centroids step, we recalculate each centroid's location as the mean (center) of all the points assigned to its cluster. We then iterate these steps until the centroids stop moving, or equivalently until the points stop switching clusters.

 -  Unfortunately, despite the fact that k-means is guaranteed to converge, the final cluster configuration to which it converges is not in general unique, and depends on the initial centroid locations

-   Lazy Learner: KNN is considered a "lazy learner" because it doesn't learn a specific model during the training phase. Instead, it memorizes the training data and makes predictions at the time of testing based on the similarity between data points.

-   Distance Metric: The choice of distance metric (e.g., Euclidean distance, Manhattan distance, etc.) is crucial in KNN. It determines how the "closeness" of data points is measured.

-   Parameter K: The hyperparameter "K" represents the number of nearest neighbors considered for making predictions. The choice of K can impact the model's performance, and it may need to be tuned based on the specific dataset and problem.

-   Decision Boundaries: In classification tasks, KNN's decision boundaries are non-linear and can adapt to complex patterns in the data. The decision is based on the majority class among the k neighbors.

-   Scalability: KNN can be computationally expensive, especially as the size of the training dataset grows. Searching for the nearest neighbors becomes more time-consuming, making it less scalable for large datasets.

-   Curse of Dimensionality: KNN can suffer from the curse of dimensionality, meaning that its performance may degrade as the number of features or dimensions increases. This is because the concept of distance becomes less meaningful in high-dimensional spaces.

-   No Training Phase: KNN does not have a traditional training phase, which means that the model quickly adapts to changes in the dataset. However, this lack of a formal training phase can also make it sensitive to noisy data.

-   Normalization: The features in the dataset should be normalized to ensure that no single feature dominates the distance calculation. Without normalization, features with larger scales can disproportionately influence the results.

-   Imbalanced Data: KNN can be sensitive to imbalanced datasets, where one class has significantly more instances than the others. Adjusting the decision rule or using weighted distances may be necessary in such cases.

-   Missing Value Handling: KNN can handle missing values by imputing them based on the values of their k nearest neighbors.

-   Practicl example [here](./k_nearest_neighbors.ipynb)

</h4>

**<h3> Support Vector Machine (SVM) </h3>**
-   
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

