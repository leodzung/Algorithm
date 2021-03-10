def numOfArrays(self, n: int, m: int, k: int) -> int:
        # dp[n][k][m]: the number of combination that has length n, cost k, and MAX element m
        dp = [[[0]*(m+1) for _ in range(k+1)] for _ in range(n+1)]
        
        # regardless of the max, if lenght=1 and cost=1, there is only 1 combination
        for mIndex in range(1, m+1):
            dp[1][1][mIndex] = 1
            
        for nIndex in range(1, n+1):
            for kIndex in range(1, k+1):
                for mIndex in range(1, m+1):
                    # We can build dp[n][k][m] from length m-1, and adding 1 more item. There are two scenarios:
                    # If we want to keep the same cost, it mean we don't jump in the last step
                    # In other word, we only add numbers that are smaller than the max, which is mIndex
                    dp[nIndex][kIndex][mIndex] += dp[nIndex-1][kIndex][mIndex] * mIndex
                    
                    # If we want to increase the cost, it mean that the last item we add has to be a new max, which is the mIndex
                    # We can build the new array from any array whose max is less than mIndex
                    dp[nIndex][kIndex][mIndex] += sum(dp[nIndex-1][kIndex-1][i] for i in range(1, mIndex))
               
        # The result will be the sum of all dp that has length n, cost k, and MAX element up to m
        return sum(dp[n][k][i] for i in range(m+1)) % (10**9+7)
