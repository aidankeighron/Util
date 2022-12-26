---
layout: script
language: Python
---

```python
print("global scope")# global scope #
number = 10

def set(value):
    number = value

def global_set(value):
    global number
    number = value

set(5)
print(number) # 10
global_set(5)
print(number) # 5

print("non local scope")# nonlocal scope #

def outer():
    result = "outer"
    
    def inner():
        result = "inner"
    
    def proper_inner():
        nonlocal result
        result = "inner"
    
    def display():
        print(result)
    
    print(result) # outer
    inner()
    print(result) # outer
    proper_inner()
    print(result) # inner
    
    return display

display = outer()
display() # inner
```