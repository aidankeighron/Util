---
layout: script
language: Algorithms
---

# Binary Search

Find the index of a item in a sorted list.

```python
def search(sorted_list, item):
    left, right = 0, len(sorted_list)-1
    while left <= right:
        midpoint = left + (right - left) // 2
        current = sorted_list[midpoint]
        if current == item:
            return midpoint
        elif item < current:
            right = midpoint - 1
        elif item > current:
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