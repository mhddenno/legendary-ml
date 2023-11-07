<h1> Feature Scaling </h1>
How to compare different types of columns - apples with oranges?!
Note: Scaling can be implemented only on columns (features)

<h2> Normalization </h2>

* $$ X^`= X - X_{min} / X_{max} - X_{min} $$
* $$ x \in [0 ; 1] $$

<h2> Standardization </h2>

* $$ X^`= X - \mu / \delta $$
* $$ x \in [-3 ; 3] $$

<h2> Example </h2>

Which two people are similar to each other more?
| People | Salary | Age |
| :-----:| :----: | --: |
| A      | 70_000 | 45  |
| B      | 60_000 | 44  |
| C      | 52_000 | 40  |

click to see [result](parts/data_preprocessing/scaling.py)