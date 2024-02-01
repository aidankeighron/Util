def combination_sum(collection: list, target: int) -> list:
    answer = []
    current = []
    def backtrack(target, previous):
        if target == 0:
            answer.append(current.copy())
            return
        for i in range(previous, len(collection)):
            if target >= collection[i]:
                current.append(collection[i])
                backtrack(target-collection[i], i)
                current.pop()
    backtrack(target, 0)
    return answer

print(combination_sum([2, 3, 5], 8))