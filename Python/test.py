def max_product_subarray(nums: list) -> int:
    
    current_max = current_min = res = nums[0]
    for i in range(1, len(nums)):
        n = nums[i]

        if n  < 0:
            current_max, current_min = current_min, current_max
        current_max = max(n, current_max * n)
        current_min = min(n, current_min * n)

        res = max(res, current_max)
    return res

print(max_product_subarray([2, 3, 2, 4]))