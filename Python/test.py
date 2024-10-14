def longest_palindromic_subsequence(string: str) -> int:
    n = len(string)
    rev = string[::-1]
    dp = [[-1]*(n+1) for _ in range(n+1)]

    for i in range(n+1):
        dp[i][0] = 0
        dp[0][i] = 0

    for i in range(1, n+1):
        for j in range(1, n+1):
            if string[i-1] == rev[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[n][n]

print(longest_palindromic_subsequence("bbabcbcab"))