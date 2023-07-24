---
layout: script
language: Python
---

Lambda expressions are used to simplify expressions and make them shorter. They are useful when needing to modify every index of a list or when needing to access nested data. Lambda expressions have numerous applications and their flexibility lets them slot in nicely to existing code.

```python
square = lambda x: x * x
print(square(4)) # 16

even_num = [lambda arg=x: arg for x in range(10) if x%2 == 0]
for num in even_num: # 0 2 4 6 8
    print(num())

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
square_list = list(map(lambda x: x * x, numbers))
print(square_list) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

max = lambda a, b: a if a > b else b
print(max(7, 4)) # 7

numbers = [[3, 5], [7, 9], [1, 2]]
# Find largest second index and return the whole list
largest = max(numbers, key=lambda x: x[1])
print(largest) # [7, 9]
```