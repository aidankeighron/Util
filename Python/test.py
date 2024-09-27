def longest_common_subsequence(x: str, y: str) -> str:
    m = len(x)
    n = len(y)

    dp = [[0] * (n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            match = 1 if x[i-1] == y[j-1] else 0

            dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]+match)

    seq = ""
    i, j = m, n
    while i > 0 and j > 0:
        match = 1 if x[i-1] == y[j-1] else 0

        if dp[i][j] == dp[i-1][j-1] + match:
            if match:
                seq = x[i-1] + seq
            i -= 1
            j -= 1
        elif dp[i][j] == dp[i-1][j]:
            i -= 1
        else:
            j -= 1

    return seq


print(longest_common_subsequence("programming", "gaming"))