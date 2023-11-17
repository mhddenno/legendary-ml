<h1> P-Value </h1>

[For introduction](./p_value_for_dummies.md)
The p-value is a measure used in statistical hypothesis testing to determine the evidence against a null hypothesis.

<h3> Statistical Hypothesis </h3>

In statistical hypothesis testing, you start with a null hypothesis (often denoted as H0) that there is no effect or no difference, and an alternative hypothesis (often denoted as H1) that there is an effect or a difference.
| Hypothesis | Description |
| -------- | -------- |
| H0 | The new drug has no effect on reducing blood pressure (mean blood pressure before = mean blood pressure after treatment). |
| H1 | The new drug is effective in reducing blood pressure (mean blood pressure after treatment is different from mean blood pressure before). |

**The p-value is the probability of obtaining results as extreme or more extreme than the observed results under the assumption that the null hypothesis is true. In other words, it quantifies the strength of the evidence against the null hypothesis.**

<h3> Example </h3>

1. Formulate Hypotheses:

| Hypothesis | Description |
| ---------- | ---------- |
| Null Hypothesis (H0) | Assumes no effect or no difference |
| Alternative Hypothesis (H1) | Assumes an effect or a difference |

2. Collect Data:
Gather relevant data through experimentation, observation, or other means. eg You collect blood pressure measurements from a sample of individuals before and after treatment with the new drug.
3. Statistical Analysis:
Use statistical methods to analyze the data and calculate a [test statistic](./t_test.md). eg Calculate the mean difference in blood pressure for the sample.
4. P-value Calculation:
The p-value is then calculated based on the test statistic and the assumed distribution under the null hypothesis. eg Use a statistical test (such as a [t-test](./t_test.md)) to calculate the p-value based on the observed mean difference and the variability in the data.
5. Interpretation:
- If the p-value is small (typically less than a predetermined significance level, often denoted as alpha, e.g., 0.05), it is considered evidence against the null hypothesis. 
- If the p-value is large, there is not enough evidence to reject the null hypothesis.
- Exempli gratia. If the p-value is less than your chosen significance level (let's say 0.05), you might conclude that there is enough evidence to reject the null hypothesis.
6. Decision:
- If the p-value is less than or equal to the chosen significance level, you may reject the null hypothesis in favor of the alternative hypothesis.
- If the p-value is greater than the significance level, you do not reject the null hypothesis.
- Exempli gratia. If the p-value is less than 0.05, you reject the null hypothesis and conclude that the new drug has a statistically significant effect on reducing blood pressure. If the p-value is greater than 0.05, you do not reject the null hypothesis.

For example, if the calculated p-value is 0.03, which is less than 0.05, you might decide to reject the null hypothesis and conclude that there is evidence to suggest that the new drug is effective in reducing blood pressure. Keep in mind that the specific test and procedures would depend on the nature of the data and the hypothesis being tested.