def canReach(self, s, minJump, maxJump):
        """
        :type s: str
        :type minJump: int
        :type maxJump: int
        :rtype: bool
        """
        # Current position is reachable or not
        dp = [c=='0' for c in s]
        
        # Number of reachable position in the previous sliding window
        pre = 0
        for i in range(1, len(s)):
            # We slide the window by 1
            # Add the right most
            if i>=minJump: pre += dp[i-minJump]
            # Subtract the left most
            if i>maxJump: pre -= dp[i-maxJump-1]
            
            dp[i] &= pre > 0
            
        return dp[-1]
