---
layout: script
language: Algorithms
---

# Fibonacci Numbers

Calculates the first `n` fibonacci numbers.

```python
def fibonacci(n):

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
def longest_common_substring(string1, string2):
    string1_len = len(string1)
    string2_len = len(string2)

    dp = [[0] * (string2_len + 1) for _ in range(string1_len_1)]
    ans_index = 0
    ans_length = 0

    for i in range(1, string1_len+1):
        for j in range(1, string2_len+1):
            if string1[i-1] == string1[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
                if dp[i][j] > ans_length:
                    ans_index = i
                    ans_length = dp[i][j]
    
    return string1[ans_index - ans_length:ans_index]
```
