def permutations(collection: list) -> list:
    res = []
    collection.sort()
    cur = []
    def dfs(i):
        if cur not in res:
            res.append(cur.copy())
        if i >= len(collection):
            return
        cur.append(collection[i])
        dfs(i+1)

        cur.pop()
        dfs(i+1)
    dfs(0)

    return res

print(permutations([1,2,3,4]))