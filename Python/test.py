def abbreviation(string: str, abbreviation: str) -> bool:
    dp = [[False for _ in range(len(abbreviation)+1)] for _ in range(len(string)+1)]
    dp[0][0] = True

    for i in range(len(string)):
        for j in range(len(abbreviation)+1):
            if dp[i][j]:
                if j < len(abbreviation) and string[i].upper() == abbreviation[j]:
                    dp[i+1][j+1] = True
                if string[i].islower():
                    dp[i+1][j] = True
    
    return dp[len(string)][len(abbreviation)]

print(abbreviation("daBcd", "ABC"))
print(abbreviation("dBcd", "ABC"))