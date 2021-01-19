# | Item | Weight | Value |
# |------|--------|-------|
# | 1    | 2      | 1     |
# | 2    | 10     | 20    |
# | 3    | 3      | 3     |
# | 4    | 6      | 14    |
# | 5    | 18     | 100   |

# Put a placeholder 0 weight, 0 value item to max
# these line up better with the 1D memoization table K
item_weights = [0, 2, 10, 3, 6, 18]
item_values = [0, 1, 20, 3, 14, 100]

n = len(item_weights)
W = 15 # total weight capacity
K = [[0 for w in range(W + 1)] for i in range(n)]

# Recurrence
for i in range(1, n):
  for w in range(1, W + 1):
    wi = item_weights[i]
    vi = item_values[i]

    if wi <= w:
      K[i][w] = max([K[i - 1][w - wi] + vi, K[i - 1][w]])
    else:
      K[i][w] = K[i - 1][w]

# Results
print("Result: ", K[n - 1][W])

## Optional: Uncomment to view the 2D table
from pandas import *
print("K table:")
print(DataFrame(K))
