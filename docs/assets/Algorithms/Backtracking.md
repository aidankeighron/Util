---
layout: script
language: Algorithms
---

# Combination Sum

Using backtracking we find all possible combinations of the collection that sum up to target.

```python
def combination_sum(collection: list, target: int) -> list:
    result = []
    current = []
    def backtrack(target, previous):
        if target == 0:
            result.append(current.copy())
            return
        for i in range(previous, len(collection)):
            if target >= collection[i]:
                current.append(collection[i])
                backtrack(target-collection[i], i)
                current.pop()
    backtrack(target, 0)
    return result
```

# All Subsequences

Finds all posable unique subsequence within `sequence` using backtracking.

```python
def all_subsequences(sequence: list) -> list:
    result = []
    def backtrack(current, index):

        if index == len(sequence):
            result.append(current.copy())
            return

        backtrack(current, index+1)
        current.append(sequence[index])
        backtrack(current, index+1)
        current.pop(0)

    backtrack([], 0)
    return result
```

# All Permutations

This loops through all possible combinations making sure to keep the length the same as the input. It keeps track of the indexes used so it does not repeat indexes and it gets every possible combination. 

```python
def all_permutations(sequence: list) -> list:
    result = []

    seen = [0 for _ in range(len(sequence))]
    def backtrack(i, current):
        if i == len(sequence):
            result.append(current.copy())
            return

        for j in range(len(sequence)):
            if not seen[j]:
                current.append(sequence[j])
                seen[j] = True
                backtrack(i+1, current)
                current.pop()
                seen[j] = False
    backtrack(0, [])

    return result
```

# Generate Parentheses

Generate `n` number of parentheses pairs.

```python
def generate_parentheses(n: int) -> list:
    result = []

    def backtrack(num_open, num_closed, current):
        if len(current) == 2 * n:
            result.append(current)
            return

        if num_open < n:
            backtrack(num_open + 1, num_closed, current + "(")
        
        if num_closed < num_open:
            backtrack(num_open, num_closed + 1, current + ")")

    backtrack(0, 0, "")
    return result
```