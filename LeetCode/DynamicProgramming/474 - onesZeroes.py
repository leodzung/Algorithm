def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # Function to count the numbers of zeros and ones
        def count(s):
            count0 = count1 = 0
            for char in s:
                if char == '0':
                    count0 += 1
                else:
                    count1 += 1
                    
            return count0, count1
        
        dp = [[0] * (n+1) for _ in range(m+1)]
        
        for s in strs:
            count0, count1 = count(s)
            for zeros in range(m, count0-1, -1):
                for ones in range(n, count1-1, -1):
                    dp[zeros][ones] = max(dp[zeros][ones], dp[zeros-count0][ones-count1]+1)
                    
        return dp[m][n]
