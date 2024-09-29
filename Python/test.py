def longest_common_substring(a: str, b: str) -> str:
    n = len(a)
    m = len(b)
    
    dp = [[0]*(m+1) for _ in range(n+1)]
    ans_index = 0 
    ans_len = 0

    for i in range(1, n+1): 
        for j in range(1, m+1):
            if a[i-1] == b[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
                if dp[i][j] > ans_len:
                    ans_index = i
                    ans_len = dp[i][j]
    
    return a[ans_index-ans_len:ans_index]

print(longest_common_substring("zxabcdezy", "yzabcdezx"))