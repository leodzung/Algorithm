def countVowelStrings(self, n: int) -> int:
        # Notice that we can append "a" to all strings w/ length(n-1) and they will become valid strings w/ length(n)
        # Also, we can modify all the strings start with "e" by making them start with "a", and they will also be valid
        # So No. of strings start with "a" and length(n) = No. of strins start with "a", length(n-1), and No. of strings start with "e", length(n)
        # Same argument can be applied for other characters. See table below until n = 3:
        #           a   e   i   o   u
        # n = 1     5   4   3   2   1
        # n = 2     15  10  6   3   1
        # n = 3     35  20  10  4   1
        
        # 6 = len(["a","e","i","o","u"]) + 1
        dp = [[0] * 6 for _ in range(n)]
        
        for i in range(n):
            # Initiate the first row for n = 1
            if i == 0:
                for j in range(6):
                    # print(n, j, 5-j)
                    dp[i][5-j] = j
            else:
                for j in range(6):
                    # Recursive per observation above
                    if j != 0:
                        dp[i][5-j] = dp[i][5-(j-1)] + dp[i-1][5-j]
        
        print(dp)
        return dp[n-1][0]
