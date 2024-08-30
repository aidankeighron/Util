def combination__sum_iv(target: int, array: list) -> int:
    def recursion(target, dp):
        if target < 0:
            return 0
        if target == 0:
            return 1
        if dp[target] != -1:
            return dp[target]
        answer = sum(recursion(target - item, dp) for item in array)
        dp[target] = answer
        return answer

    dp = [-1] * (target+1)
    return recursion(target, dp)

print(combination__sum_iv(5, [5, 3, 9, 9]))