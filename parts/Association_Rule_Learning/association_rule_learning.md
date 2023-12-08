**<h3> People who bought also bought! </h3>**

<h4> Apriori </h4>

-   A classic algorithm in data mining and machine learning
-   Can we prove that you will (buy/like/...) depending on prior knowledge
-   Main points: 
-   - $ support(x)= \#userWatchListsContainting(x)/\#userWatchLists $
-   - $ confidence(x_1 -> x_2)= \#userWatchListsContainting(x_1 \&\ x_2)/\#userWatchListsContainting(x_1) $
-   - $ lift $ Is the imporovment of your orginal predection $ lift(x_1 -> x_2) = support(x_1 \&\ x_2) / suppport(x_1) * support(x_2) $
-   Alogrithm:
-   - Set a minimum support and confidence
-   - Calculate all the subsets in transactions having higher support than minimum support
-   - Calculate all the rules of these subsets having higher confidence than minimum confidence
-   - Sort the rules by decreasing lift

<h4> Eclat </h4>

-   
-   
-   