<h1> P-Value </h1>

The p-value is a measure used in statistical hypothesis testing to determine the evidence against a null hypothesis.

<h3> Statistical Hypothesis </h3>

Assume those two possible/alternative worlds/situations a world with fair coin and one without a fair coin and we need to know the truth :) where do i live?

| Hypothesis | Description |
| -------- | -------- |
| H0 | This is a fair coin. |
| H1 | This is not a fair coin. |

**I assume i live in a world with H0:**
- I start to throw the coin
- First throw we got H (0.5) ==> it is okay
- Second throw we got H (0.5 * 0.5 = 0.25) ==> it could happen the probability is low
- Third throw we got H (0.5 * 0.5 * 0.5 = 0.12) ==> okay that's strange if we are in the H0 universe
- Fourth throw we got H (0.5 * 0.5 * 0.5 * 0.5 = 0.06) ==> something not right is happening
- Fifth throw we got H (0.5 * 0.5 * 0.5 * 0.5 * 0.5 = 0.03) ==> okay i am very special becuase i have seen something happens with a very low probability 
- Sixth throw we got H (0.5 * 0.5 * 0.5 * 0.5 * 0.5 * 0.5 = 0.01) ==> okay i can't be living in H0 (I have rejected the null hypothesis)

**so (0.5 > 0.25 > 0.12 > 0.06 > 0.03 > 0.01) is the p-value**

but how to define mathematically that i don't have an easy feeling about that? 
we should define a (statistical significance, alpha, confidence lever = 0.05) which means after this alpha I am confident to reject the H0 universe
