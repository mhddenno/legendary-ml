<h1> Building A Model </h1>

* garbage in = garbage out
* using the right feature

<h2> All-in </h2>

* Throw all the data in
* Prior knowledge
* You have to
* Preparing for Backward Elimination

<h2> Backward Elimination (Stepwise Regression) </h2>

* Select a significant level to stay in the model (sl = 0.005)
* Fit the full model with all possible predictors
* Consider the predictor with the highest [P-value](../statistics/p_value.md). If P > sl go to step 4, otherwise go to FIN
* Remove the predictor
* Fit model without this variable

<h2> Forward Selection (Stepwise Regression) </h2>

* Select a significance level to enter the model (sl = 0.05)
* Fit all simple regression models $$ Y = X_{n} $$ Select the one with the lowest [P-value](../statistics/p_value.md)
* Keep this variable and fit all possible models with one extra predictor added to the one(s) you already have
* Consider the predictor with the lowest P-value. If P < sl, go to Step 3, otherwise go to FIN (keep the previous model because the last varialbe is insignificant )

<h2> Bidirectional Elimination (Stepwise Regression) </h2>

* Select a significance lever to enter and to stay in the model (eg: sl_enter = 0.05, sl_stay = 0.05)
* Perform the next step of forward selection (new variables must have: p < sl_enter to enter)
* Perform ALL steps of backward elimination (old variables must have p < sl_stay to stay)
* No new variables can enter and no old variables can exit

<h2> Score Comparison (All possible models)</h2>

* Select al criterion of goodness of fit
* Construct all possible regression models: $$ 2^N-1 $$
* Select the one with the best criterion
* Example: 10 columns means 1023 models
