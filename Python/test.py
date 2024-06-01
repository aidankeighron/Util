def max_subarray(arr: list) -> list:

    def max_cross_sum(low, mid, high):
        cross_sum = 0
        left_sum, max_left = float("-inf"), -1
        right_sum, max_right = float("-inf"), -1
        
        for i in range(mid, low-1, -1):
            cross_sum += arr[i]
            if cross_sum > left_sum:
                left_sum = cross_sum
                max_left = i

        cross_sum = 0
        for i in range(mid+1, high+1):
            cross_sum += arr[i]
            if cross_sum > right_sum:
                right_sum = cross_sum
                max_right = i

        return max_left, max_right, (left_sum + right_sum)

    def subarray(low, high):
        if low == high:
            return low, high, arr[low]

        mid = (low + high) // 2
        left_low, left_high, left_sum = subarray(low, mid)
        right_low, right_high, right_sum = subarray(mid+1, high)
        cross_left, cross_right, cross_sum = max_cross_sum(low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        return cross_left, cross_right, cross_sum

    res = subarray(0, len(arr)-1)
    return arr[res[0]:res[1]+1]

print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))