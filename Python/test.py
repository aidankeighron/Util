def peak(arr: list) -> int:
    mid = len(arr) // 2
    three = arr[mid-1:mid+2]

    if three[1] > three[0] and three[1] > three [2]:
        return three[1]
    elif three[0] < three[2]:
        if len(arr[:mid]) == 2:
            m -= 1
        return peak(arr[mid:])
    else:
        if len(arr[:mid]) == 2:
            m += 1
        return peak(arr[:mid])

print(peak([1, 2, 3, 4, 5, 4, 3, 2, 1]))