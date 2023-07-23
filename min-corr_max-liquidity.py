import pandas as pd
import itertools

# Path to the CSV file containing the data
path_corr = ""

# List of currency pairs to filter the DataFrame
list_pairs = ["EURUSD", "GBPUSD", "NZDUSD", "EURJPY", "AUDUSD", "USDCAD", "USDCHF", "GBPJPY", "EURGBP", "AUDJPY", "EURAUD"]

# Dictionary containing currency pairs as keys and their respective values
dict_pairs = {
    "EURUSD": 0.28,
    "GBPUSD": 0.13,
    "NZDUSD": 0.11,
    "EURJPY": 0.04,
    "AUDUSD": 0.06,
    "USDCAD": 0.05,
    "USDCHF": 0.05,
    "GBPJPY": 0.04,
    "EURGBP": 0.03,
    "AUDJPY": 0.03,
    "EURAUD": 0.02
}

# Read the CSV file and filter rows based on the 'pair1' or 'pair2' column containing currency pairs from 'list_pairs'
df = pd.read_csv(path_corr)
filtered_df = df[(df['pair1'].isin(list_pairs) | df['pair2'].isin(list_pairs)) & df['pair2'].isin(list_pairs)]

# Create two new columns 'liquidity_pair_1' and 'liquidity_pair_2' in the DataFrame 'filtered_df'
filtered_df['liquidity_pair_1'] = filtered_df['pair1'].map(dict_pairs)
filtered_df['liquidity_pair_2'] = filtered_df['pair2'].map(dict_pairs)

# Create the sum of liquidity
filtered_df['sum_liquidity'] = filtered_df['liquidity_pair_1'] + filtered_df['liquidity_pair_2']

# Generate all possible combinations of 5 currency pairs
combinations = list(itertools.combinations(list_pairs, 5))

# Find the group that maximizes the sum of liquidity and minimizes the sum of correlation
best_group = None
max_sum_liquidity = float('-inf')
min_sum_correlation = float('inf')

timeframe = "1h"
for group in combinations:
    # Filter the rows in the DataFrame for the current group
    selected_rows = (filtered_df['pair1'].isin(group)) & (filtered_df['pair2'].isin(group))
    sum_liquidity = filtered_df.loc[selected_rows, 'sum_liquidity'].sum()
    sum_correlation = filtered_df.loc[selected_rows, timeframe].abs().sum()

    if sum_liquidity > max_sum_liquidity or (sum_liquidity == max_sum_liquidity and sum_correlation < min_sum_correlation):
        max_sum_liquidity = sum_liquidity
        min_sum_correlation = sum_correlation
        best_group = group

print("Best group of currency pairs:")
print(best_group)
print("Sum of liquidity in the group:")
print(max_sum_liquidity)
print("Sum of correlation in the group:")
print(min_sum_correlation)
