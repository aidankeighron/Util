def largest_divisible_subset(array: list) -> list:
    array.sort()

    memo = [1] * len(array)
    hash_array = list(range(len(array)))

    for i, item in enumerate(array):
        for prev in range(i):
            if array[prev] != 0 and item % array[prev] == 0 and 1 + memo[prev] > memo[i]:
                memo[i] = 1 + memo[prev]
                hash_array[i] = prev

    largest = -1
    largest_index = -1

    for i, item in enumerate(memo):
        if item > largest:
            largest = item
            largest_index = i
    
    if largest_index == -1:
        return []
    result = [array[largest_index]]
    while hash_array[largest_index] != largest_index:
        largest_index = hash_array[largest_index]
        result.append(array[largest_index])

    return result


print(largest_divisible_subset([1, 16, 7, 8, 4]))