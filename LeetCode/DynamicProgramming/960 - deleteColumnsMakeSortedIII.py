# The idea is to count the number of characters to keep instead of the number of characters to remove 
    def minDeletionSize(self, strs: List[str]) -> int:
        # Length of the strings
        n = len(strs[0])
        
        # Dynamic Programming array
        dp = [1 for _ in range(n)]
        
        # We go from the end of the string backward to the start
        for i in range(n-2, -1, -1):
            
            # If all the following characters of the current characters are all smaller, we keep this character
            for j in range(i+1, n):
                if all(s[i] <= s[j] for s in strs):
                    # Add one to the previous max, we will have the current maximum number of characters to keep
                    dp[i] = max(dp[i], dp[j]+1)
                    
        # Extract maximum of the number of characters to keep, we will get the minimum number of characters to remove
        return n - max(dp)
