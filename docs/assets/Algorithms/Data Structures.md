---
layout: script
language: Algorithms
---

# Permutations

Using a depth first search this algorithm creates a list of all possible reordering of a list. It does this by recursively testing all options.

```python
def permutations(collection: list) -> list:
    res = []
    collection.sort()
    cur = []
    def dfs(i):
        if cur not in res:
            res.append(cur.copy())
        if i >= len(collection):
            return
        cur.append(collection[i])
        dfs(i+1) # find all permutations with i

        cur.pop()
        dfs(i+1) # find all permutations without i
    dfs(0)

    return res
```

## Equilibrium Index in Array

Find the index where the right and left sections of an array are equal in sum.

```python
def equilibrium_index(arr: list) -> int:
    total_sum = sum(arr)
    left_sum = 0
    for i, value in enumerate(arr):
        total_sum -= value
        if left_sum == total_sum:
            return i
        left_sum += value
    return -1
```