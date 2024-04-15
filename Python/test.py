def list_prime(n: int) -> list:
    primes = []
    if n > 1:
        primes.append(1)
    if n > 2:
        primes.append(2)
    numbers = (i for i in range(1, (n+1), 2))
    for i in (n for n in numbers if n > 1):
        bound = int(i**0.5) + 1
        for j in range(3, bound, 2):
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes

print(list_prime(11))
