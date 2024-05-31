

def max_difference(arr: list) -> tuple[int, int]:
    if len(arr) == 1:
        return arr[0], arr[0]

    first = arr[:len(arr)//2]
    second = arr[len(arr)//2:]

    small_1, big_1 = max_difference(first)
    small_2, big_2 = max_difference(second)

    min_first = min(first)
    max_second = max(second)

    if big_2 - small_2 > max_second - min_first and big_2 - small_2 > big_1 - small_1:
        return small_2, big_2
    elif big_1 - small_1 > max_second - min_first:
        return small_1, big_1
    else:
        return min_first, max_second

print(max_difference([5, 11, 2, 1, 7, 9, 0, 7]))