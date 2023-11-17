<h1> T-Test </h1>

A t-test is a statistical method used to determine if there is a significant difference between the means of two groups.
[The relationship between p-value and t-value](./t_test.ipynb)

1. Scenario

Suppose you want to investigate whether there is a significant difference in the exam scores of two different groups of students (Group A and Group B). You have the exam scores of 20 students from each group.

| Hypothesis | Description |
| -------- | -------- |
| H0 | There is no significant difference in the mean exam scores between Group A and Group B |
| H1 | There is a significant difference in the mean exam scores between Group A and Group B |

2. Collect Data:
Record the exam scores of 20 students from Group A and 20 students from Group B.
3. Statistical Analysis:
Calculate the mean and standard deviation for each group.
4. Formulate the Test Statistic:

$$ t = \frac{{\bar{X}_1 - \bar{X}_2}}{{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}}} $$

where:
- \( \bar{X}_1\) and \(\bar{X}_2\) are the sample means for Group A and Group B, respectively.
- \(s_1\) and \(s_2\) are the sample standard deviations for Group A and Group B, respectively.
- \(n_1\) and \(n_2\) are the sample sizes for Group A and Group B, respectively.

5. P-value Calculation:
Use the t-statistic to calculate the p-value. This involves referring to a t-distribution table or using statistical software.
6. Interpretation:
- If the p-value is less than your chosen significance level (e.g., 0.05), you reject the null hypothesis.
- If the p-value is greater than or equal to the significance level, you do not reject the null hypothesis.
7. Decision:
- Based on the p-value, decide whether there is enough evidence to conclude that there is a significant difference in the mean exam scores between Group A and Group B.

For example, if the calculated p-value is 0.03, which is less than 0.05, you might decide to reject the null hypothesis and conclude that there is evidence to suggest that the new drug is effective in reducing blood pressure. Keep in mind that the specific test and procedures would depend on the nature of the data and the hypothesis being tested.