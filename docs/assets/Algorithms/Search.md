---
layout: script
language: Algorithms
---

# Binary Search

Find the index of a item in a sorted list.

```python
def search(sorted_list, target):
    left, right = 0, len(sorted_list)-1
    while left <= right:
        midpoint = left + (right - left) // 2
        current = sorted_list[midpoint]
        if current == target:
            return midpoint
        elif target < current:
            right = midpoint - 1
        elif target > current:
            left = midpoint + 1
    return -1
```

Breakdown:

```python
search([1,2,3,4,5], 4)

# Loop 1
left = 0
right = 4
midpoint = 0 + (4 - 0) // 2 = 2
current = sorted_list[midpoint] = 3
item > current -> left = midpoint + 1 = 3 

# Loop 2
left = 3
right = 4
midpoint = 3 + (4 - 3) // 2 = 3
current = sorted_list[midpoint] = 4
item == current -> return 3 
```

# Fibonacci Search

Searching algorithm that used the fibonacci sequence to narrow search range.
[Video Explanation](https://www.youtube.com/watch?v=GAafWFRGP7k)

```python
from functools import lru_cache

@lru_cache
def fibonacci(k):
    if k == 0:
        return 0
    if k == 1:
        return 1
    else:
        return fibonacci(k - 1) + fibonacci(k - 2)

def fibonacci_search(arr, target):
    i = 0
    len_list = len(arr)
    while True:
        if fibonacci(i) >= len_list:
            fibb_k = i
            break
        i += 1
    offset = 0
    while fibb_k > 0:
        index_k = min(offset + fibonacci(fibb_k -1), len_list - 1)
        item_k_1 = arr[index_k]
        if item_k_1 == target:
            return index_k
        elif target < item_k_1:
            fibb_k -= 1
        elif target > item_k_1:
            offset += fibonacci(fibb_k -1)
            fibb_k -= 1
    else:
        return -1
```