def knightDialer(self, n):
        """
        :type n: int
        :rtype: int
        """
        phoneMap = {0: (4, 6), 1: (6, 8), 2: (7, 9), 3: (4, 8), 4: (0, 3, 9), 6: (0, 1, 7), 7: (2, 6), 8: (1, 3), 9: (2, 4)}
        dp = [[0] * 10 for _ in range(n+1)]
        for i in range(10):
            dp[1][i] = 1
            
        for i in range(2, n+1):
            for j in range(10):
                if j in phoneMap:
                    for k in phoneMap[j]:
                        dp[i][j] += dp[i-1][k]
        
        return sum(dp[-1]) % (10**9 + 7)
