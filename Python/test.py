def longest_common_substring(string1, string2):
    string1_len = len(string1)
    string2_len = len(string2)

    dp = [[0] * (string2_len+1) for _ in range(string1_len+1)]
    ans_index = 0
    ans_length = 0

    for i in range(1, string1_len+1):
        for j in range(1, string2_len+1):
            if string1[i-1] == string2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
                if dp[i][j] > ans_length:
                    ans_index = i
                    ans_length = dp[i][j]
    
    return string1[ans_index - ans_length:ans_index]

print(longest_common_substring("abc", "abc"))