def power(x: int, a: int):
    if not a:
        return 1
    if a % 2 == 0:
        return power(x, a//2) * power(x, a//2)
    return x * power(x, a//2) * power(x, a//2)

print(power(3, 2))
print(power(5, 3))