def factorial(n: int) -> int:
    value = 1
    for i in range(1, n+1):
        value *= i
    return value

print(factorial(100))