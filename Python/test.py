def heaps(arr: list) -> list:
    res = []

    def generate(k, subset):
        if k == 1:
            res.append(subset[:])
            return

        generate(k-1, subset)

        for i in range(k-1):
            if k % 2 == 0:
                subset[i], subset[k-1] = subset[k-1], subset[i]
            else:
                subset[0], subset[k-1] = subset[k-1], subset[0]
            generate(k-1, subset)
    
    generate(len(arr), arr)
    return res

print(heaps([1,2,3]))