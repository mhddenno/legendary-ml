<h1>R2 and adjusted R2</h1>
<h3>
R-squared (R2) and adjusted R-squared (adjusted R2) are both metrics used in regression analysis to evaluate the goodness of fit of a model. However, they serve slightly different purposes.
</h3>

<h3>
R-squared (R2):
</h3>

<h4>

- R-squared is a measure of the proportion of the variance in the dependent variable that is explained by the independent variables in the model.
- It ranges from 0 to 1, where 0 indicates that the model does not explain any of the variability in the dependent variable, and 1 indicates that the model explains all of the variability.
- R-squared tends to increase as more independent variables are added to the model, even if they do not contribute significantly to explaining the variance. Therefore, it does not penalize the inclusion of irrelevant variables.
- $$ R2 = 1 - (Sum of Squared Residuals / Total Sum of Squares) $$
</h4>

<h3>
Adjusted R-squared (adjusted R2):
</h3>

<h4>

- Adjusted R-squared takes into account the number of predictors in the model, penalizing the inclusion of unnecessary variables that do not contribute significantly to explaining the variance.
- It is especially useful when comparing models with different numbers of predictors.
- Adjusted R-squared will be lower than R-squared if the added variables do not improve the model's performance.
- $$ Adjusted R2 = 1 - [(1 - R2) * (n - 1) / (n - k - 1)] $$

</h4>

<h3>

[Visualising](../../res/r_error.pdf)

</h3>