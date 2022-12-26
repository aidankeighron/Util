---
layout: script
language: Python
---

```python
def sequence():
    for i in range(5):
        yield i
        
result = sequence()
print(next(result)) # 0
print(next(result)) # 1
print(next(result)) # 2

sequence = (i for i in range(5))

for value in sequence: # 0 1 2 3 4
    print(value)
```

