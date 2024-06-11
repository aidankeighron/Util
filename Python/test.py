def merge_sort(arr: list) -> list:
    
    def merge(left, right):
        res = []
        while left and right:
            res.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
        res.extend(left)
        res.extend(right)
        return res
    
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))

print(merge_sort([0, 5, 3, 2, 2]))