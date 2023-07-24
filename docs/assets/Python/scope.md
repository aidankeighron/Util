---
layout: script
language: Python
---

Scope is all about what variables you can access and when. Global variables (variables outside of any method) can be read from inside methods but need the global keyword to be written to. The same goes for local variables in the context of nested methods.

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