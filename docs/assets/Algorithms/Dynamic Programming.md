---
layout: script
language: Algorithms
---

# Fibonacci Numbers

Calculates the first `n` fibonacci numbers.

```python
def fibonacci(n: int) -> list:

    if n == 0:
        return [0]
    fib = [0, 1]
    for _ in range(n-1):
        fib.append(fib[-1]+fib[-2])
    return fib
```

# Longest Common Substring

Finds the longest common substring between two strings.

```python
def longest_common_substring(string1: str, string2: str) -> str:
    string1_len = len(string1)
    string2_len = len(string2)

    dp = [[0] * (string2_len+1) for _ in range(string1_len+1)]
    ans_index = 0
    ans_length = 0

    for i in range(1, string1_len+1):
        for j in range(1, string2_len+1):
            if string1[i-1] == string2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
                if dp[i][j] > ans_length:
                    ans_index = i
                    ans_length = dp[i][j]
    
    return string1[ans_index - ans_length:ans_index]
```

Explanation:

Using the 2d array `dp` the program keeps track of the number of same characters in a row:

```python
longest_common_substring("abc", "abc")

dp = [
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 2, 0],
    [0, 0, 0, 3]
]

output = "abc"
```

# Knapsack

Finds the max value that can be put into the knapsack taking into account the capacity and weights of the objects. I uses recursion to find if an object can be put in the knapsack optimally or if it needs to be omitted.

```python
def knapsack(capacity: int, weights: list, values: list, counter: int) -> int:

    if capacity == 0 or counter == 0:
        return 0

    if weights[counter - 1] > capacity:
        return knapsack(capacity, weights, values, counter - 1)
    else:
        left_capacity = capacity - weights[counter - 1]
        new_value = values[counter - 1] + knapsack(left_capacity, weights, values, counter - 1)
        without_value = knapsack(capacity, weights, values, counter - 1)
        return max(new_value, without_value)
```

# Minimum Cost Path

Find the lowest "cost" from top left of a matrix to the bottom right. This works by choosing to either move down or right depending on the lowest cost.

```python
def minimum_cost_path(matrix: list[list]) -> int:
    # first row
    for i in range(1, len(matrix[0])):
        matrix[i][i] += matrix[0][i-1]

    # first column
    for i in range(1, len(matrix)):
        matrix[i][0] += matrix[i - 1][0]

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            matrix[i][j] += min(matrix[i-1][j], matrix[i][j-1])

    return matrix[-1][-1]
```

# Longest Palindrome Sequence

Finds the longest palindrome sequence in a string. Using a dp matrix to keep track of matching characters.

```python
def longest_palindrome_sequence(string: str) -> int:
    n = len(string)
    reverse = string[::-1]
    dp = [[-1] * (n+1) for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 0
        dp[0][i] = 0

    for i in range(1, n+1):
        for j in range(1, n+1):
            if string[i-1] == reverse[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[n][n]
```