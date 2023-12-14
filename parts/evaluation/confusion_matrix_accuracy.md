<h1>Confusion matrix and APRSF1 Used for Classification models evaluation</h1>
<h4>
A confusion matrix is a table that is used to evaluate the performance of a classification algorithm.

-   True Positives (TP): The number of instances where the model correctly identified the positive class.

-   True Negatives (TN): The cases where the model correctly identified the negative class.

-   False Positives (FP): These are the cases where the model predicted a positive outcome, but the true class was negative.

-   False Negatives (FN): This refers to the cases where the model predicted a negative outcome, but the true class was positive.
</h4>
<h3>

|     | Actual Positive | Actual Negative |
| --- | --------------- | --------------- |
| Predicted Positive  | TP      | FP       |
| predeicted Negative | FN   | TN        |

</h3>

**<h3> APRSF1 </h3>**
**Accuracy:**
It calculates the ratio of correctly predicted instances to the total instances.
-   Use Case: When classes are balanced, and false positives and false negatives have similar consequences.
-   Scenario: Accuracy is a good overall measure of correct predictions. However, it may not be suitable for imbalanced datasets where one class is significantly more prevalent than the other.
$$ Accuracy = TP+TN/TP+TN+FP+FN $$

**Precision:**
Precision is the ratio of true positives to the total predicted positives. 
-   Use Case: When the cost of false positives is high or when you want to minimize false positives.
-   Scenario: For example, in spam email detection, you want to avoid marking legitimate emails as spam.
$$ Precision = TP / TP + FP $$

**Recall (True Positive Rate or Sensitivity):**
Recall is the ratio of true positives to the total actual positives.
-   Use Case: When the cost of false negatives is high or when you want to minimize false negatives.
-   Scenario: When the goal is to capture as many positive instances as possible, even if it means accepting more false positives. For instance, in a medical diagnosis scenario, you want to ensure that you don't miss any positive cases, even if it results in more false alarms.
$$ Recal = TP / TP + FN $$

**Specificity (True Negative Rate):**
The proportion of true negative predictions out of the total actual negatives.
$$ Sensitivity = TN /TN + FP $$

**F1_Score:**
-   Use Case: When there is an uneven class distribution, and you want to balance precision and recall.
-   Scenario: The F1 Score is the harmonic mean of precision and recall, providing a balanced measure that is useful in situations where precision and recall have trade-offs. It's particularly relevant for imbalanced datasets or when false positives and false negatives are of similar concern.
$$ 2 * ((Recall + Precision) / (Recall * Precision)) $$