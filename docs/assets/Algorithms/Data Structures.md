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

## Product Sum

Product sum of an array is the sum of the array multiplied by their depths

```python
def product_sum(arr: list, depth: int) -> int:
    res = 0
    for x in arr:
        res += product_sum(x, depth+1) if isinstance(x, list) else x
    return res * depth
```

## Find Triplets with 0 Sum

Finds three numbers that add up to zero by finding two and seeing if there exists a number that when added to them results in zero

```python
def find_triplets_with_0_sum(arr: list) -> set:
    res = set()
    for i, item in enumerate(arr[:-2]):
        seen = set()
        for other in arr[i+1:]:
            to_find = -other-item
            if to_find in seen:
                res.add(tuple(sorted([item, other, to_find])))
            seen.add(other)
    return res
```

## Kth Largest Element

Finds the `position` largest element in `arr`.

```python
def kth_largest_element(arr: list, position: int) -> int:
    low, high = 0, len(arr) - 1

    def pivot_index():
        pivot = arr[high]
        i = low
        for j in range(low, high):
            if arr[j] >= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[high] = arr[high], arr[i]
        return i

    while low <= high:
        if low > len(arr) - 1 or high < 0:
            return -1
        index = pivot_index()
        if index == position - 1:
            return arr[index]
        elif index > position - 1:
            high = index - 1
        else:
            low = index + 1
```     