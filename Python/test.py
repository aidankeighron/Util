
def equilibrium_index(arr: list) -> int:
    total_sum = sum(arr)
    left_sum = 0
    for i, value in enumerate(arr):
        total_sum -= value
        if left_sum == total_sum:
            return i
        left_sum += value
    return -1

print(equilibrium_index([-7, 1, 5, 2, -4, 3, 0]))