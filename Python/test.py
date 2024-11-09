def maximum_non_adjacent_sum(nums: list) -> int:
    max_including = nums[0]
    max_excluding = 0

    for num in nums[1:]:
        max_including, max_excluding = max_excluding + num, max(max_including, max_excluding)

    return max(max_excluding, max_including) 

print(maximum_non_adjacent_sum([1, 5, 3, 7, 2, 2, 6]))