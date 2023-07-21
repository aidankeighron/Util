---
layout: script
language: Python
---

Decorators are used to add extra functionality onto existing methods.

```python
def square(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        return result*result
    return wrapper

@square
def add(x, y):
    return x + y

print(add(2, 2)) # 16

def header(string):
    def decorate(fn):
        def wrapper(*args, **kwargs):
            result = fn(*args, **kwargs)
            return string + str(result*result)
        return wrapper
    return decorate

@header("Answer: ")
def subtract(x, y):
    return x - y

print(subtract(10, 4)) # Answer: 36

class Header:
    def __init__(self, string):
        self.string = string
        
    def __call__(self, fn):
        def wrapper(*args, **kwargs):
            result = fn(*args, **kwargs)
            return self.string + str(result)
        return wrapper
    
@Header("Result: " )
def divide(x, y):
    return x/y

print(divide(10, 2)) # Result: 5.0
divide_header = Header("Answer: ")(divide)
print(divide_header(12, 2)) # Answer: 6.0
```