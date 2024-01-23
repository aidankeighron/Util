---
layout: script
language: Algorithms
---

# Bubble Sort

Moves all the largest elements to the right

```python
def bubble_sort(collection):
    length = len(collection)

    for i in reversed(range(length)):
        swapped = False
        for j in range(i):
            if collection[j] > collection [j + 1]:
                swapped = True
                collection[j], collection[j + 1] = collection[j + 1], collection[j]
            if not swapped:
                break
    return collection
```

Breakdown:

```python
bubble_sort([4,1,3,2])

# Outer Loop 1
# [1, 4, 3, 2]
# [1, 3, 4, 2]
# [1, 3, 2, 4]

# Outer Loop 2
# [1, 3, 2, 4]
# [1, 2, 3, 4]
```

# Quick Sort

Quick sort uses a pivot and sorts all greater numbers to the right of the pivot and all lesser numbers to the left. Doing this recursively will eventually get a sorted list.

```python
from random import randrange

def quick_sort(collection):
    length = len(collection)

    if length < 2:
        return collection

    pivot_index = randrange(length)
    pivot = collection.pop(pivot_index)

    lesser = [item for item in collection if item <= pivot]
    greater = [item for item in collection if item > pivot]

    return [*quick_sort(lesser), pivot, *quick_sort(greater)]

```

Breakdown:

```python
quick_sort([5,1,3,2])

# Loop 1
input = [5,1,3,2]
pivot = 2
[*lesser, pivot, *greater] = [1, 2, 5, 3]

# Loop 2
input = [5, 3]
pivot = 5
[*lesser, pivot, *greater] = [3, 5]

# Loop 3
input = [1]
len < 2

output = [1, 2, 3, 5]
```