def sum_of_subsets(numbers: list, target_sum: int) -> list:
    result = []

    def backtrack(i, path, remaining_sum):
        if sum(path) > target_sum or (remaining_sum + sum(path)) < target_sum:
            return
        if sum(path) == target_sum:
            result.append(path.copy())
            return
        for j in range(i, len(numbers)):
            backtrack(j+1, [*path, numbers[j]], remaining_sum - numbers[j])

    backtrack(0, [], sum(numbers))
    return result

print(sum_of_subsets([3, 34, 4, 12, 5, 2], 9))