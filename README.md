# Currency Pair Subset Selection Optimization

Suppose we have a set of currency pairs $C$, and our goal is to select a subset $G$ of 5 currency pairs from $C$ to achieve two objectives:

1. **Maximize the sum of liquidity**: Liquidity refers to the ability to convert an asset (currency pair in this case) into cash quickly without causing significant price changes. For each combination $G$ of 5 currency pairs, we calculate the liquidity $x_i$ associated with each currency pair $i$ in $G$. The liquidity $x_i$ is typically a positive value representing the trading volume or market depth of currency pair $i$ in $G$. The sum of liquidity for the group $G$ is denoted as $\text{sum\_liquidity}(G) = \sum_{i \in G} x_i$. Our objective is to find the subset $G^*$ that maximizes the sum of liquidity $\text{sum\_liquidity}(G^*)$.

2. **Minimize the sum of correlation**: Correlation refers to the degree of association between the price movements of two currency pairs. For each combination $G$ of 5 currency pairs, we calculate the correlation $y_i$ associated with each currency pair $i$ in $G$. To simplify the optimization problem, we consider the absolute value of the correlation $|y_i|$ so that we only care about the strength of the relationship, not its direction. The sum of correlation for the group $G$ is denoted as $\text{sum\_correlation}(G) = \sum_{i \in G} |y_i|$. Our objective is to find the subset $G^*$ that minimizes the sum of correlation $\text{sum\_correlation}(G^*)$.

The optimization problem can be mathematically formulated as follows:
Find \(G^*\) such that:

\[
G^* = \underset{G \in \text{combinations}}{\text{argmax}} \left( \sum_{i \in G} x_i \right)
\]

subject to:

\[
\text{sum\_correlation}(G^*) = \underset{G \in \text{combinations}}{\text{min}} \left( \sum_{i \in G} |y_i| \right)
\]

Once the optimization problem is solved, $G^*$ will represent the group of 5 currency pairs that maximizes the sum of liquidity and minimizes the sum of correlation, and $\text{sum\_liquidity}(G^*)$ and $\text{sum\_correlation}(G^*)$ will represent the maximum sum of liquidity and minimum sum of correlation, respectively.
