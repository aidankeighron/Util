def number_of_binary_trees(nodes: int) -> int:
    def factorial(n):
        out = 1
        for i in range(1, n+1):
            out *= i
        return out
    
    def catalan_number(n):
        out = 1
        for i in range(n):
            out *= 2*n-i
            out //= i+1
        return out // (n+1)
        

    return factorial(nodes) * catalan_number(nodes)
print(number_of_binary_trees(6))