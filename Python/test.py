def find_triplets_with_0_sum(arr: list) -> set:
    res = set()
    for i, item in enumerate(arr[:-2]):
        seen = set()
        for other in arr[i+1:]:
            to_find = -other-item
            if to_find in seen:
                res.add(tuple(sorted([item, other, to_find])))
            seen.add(other)
    return res

print(find_triplets_with_0_sum([-1, 0, 1, 2, -1, -4]))