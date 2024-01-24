---
layout: script
language: Algorithms
---

# Fibonacci Numbers

Calculates the first `n` fibonacci numbers.

```python
def fibonacci(n):

    if n == 0:
        return [0]
    fib = [0, 1]
    for _ in range(n-1):
        fib.append(fib[-1]+fib[-2])
    return fib
```

