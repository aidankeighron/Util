from random import choice

def kth_number(arr: list, k: int) -> int:
    pivot = choice(arr)

    smaller = [i for i in arr if i < pivot]
    bigger = [i for i in arr if i > pivot]

    if len(smaller) == k -1:
        return pivot
    elif len(smaller) < k - 1:
        return kth_number(bigger, k - len(smaller) - 1)
    else:
        return kth_number(smaller, k)

print(kth_number([25, 21, 98, 100, 76, 22, 43, 60, 89, 87], 4))