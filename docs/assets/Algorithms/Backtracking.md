---
layout: script
language: Algorithms
---

# Combination Sum

Using backtracking we find all possible combinations of the collection that sum up to target.

```python
def combination_sum(collection: list, target: int) -> list:
    answer = []
    current = []
    def backtrack(target, previous):
        if target == 0:
            answer.append(current.copy())
            return
        for i in range(previous, len(collection)):
            if target >= collection[i]:
                current.append(collection[i])
                backtrack(target-collection[i], i)
                current.pop()
    backtrack(target, 0)
    return answer
```

# All Subsequences

Finds all posable unique subsequence within `sequence` using backtracking.

```python
def all_subsequences(sequence: list) -> list:
    answer = []
    def backtrack(current, index):

        if index == len(sequence):
            answer.append(current.copy())
            return

        backtrack(current, index+1)
        current.append(sequence[index])
        backtrack(current, index+1)
        current.pop(0)

    backtrack([], 0)
    return answer
```
