def catalan_numbers(n: int) -> list:
    catalan = [0] * (n+1)
    catalan[0] = 1
    
    if n > 0:
        catalan[1] = 1

    for i in range(2, n+1):
        for j in range(i):
            catalan[i] += catalan[j] * catalan[i-j-1]

    return catalan 

print(catalan_numbers(10))