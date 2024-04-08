def kth_largest_element(arr: list, position: int) -> int:
    low, high = 0, len(arr) - 1

    def pivot_index():
        pivot = arr[high]
        i = low
        for j in range(low, high):
            if arr[j] >= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[high] = arr[high], arr[i]
        return i

    while low <= high:
        print(arr)
        if low > len(arr) - 1 or high < 0:
            return -1
        index = pivot_index()
        if index == position - 1:
            return arr[index]
        elif index > position - 1:
            high = index - 1
        else:
            low = index + 1

print(kth_largest_element([3.1, 1.2, 5.6, 4.7,7.9,5,0], 2))