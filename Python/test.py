def all_subsequences(sequence: list) -> list:
    answer = []
    def backtrack(current, index):

        if index == len(sequence):
            answer.append(current.copy())
            return

        backtrack(current, index+1)
        current.append(sequence[index])
        backtrack(current, index+1)
        current.pop(0)

    backtrack([], 0)
    return answer

print(all_subsequences([2, 3, 5]))