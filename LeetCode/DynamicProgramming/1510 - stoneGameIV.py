def winnerSquareGame(self, n: int) -> bool:
        """
        The idea is to explore all the winning states from all the losing state
        If one state is losing and there is a move, Alice make that move and Bob will fall into the losing state
        Using dynamic programming because:
        Base case: Winning state in 1 move - all the square numbers
        Next case: Losing state + 1 move
        """
        dp = [0 for _ in range(n+1)]
        
        # Explore all the states
        for i in range(n+1):
            # If this is a winning state, stop exploring
            if dp[i]:
                continue
                
            # If this is a losing state, explore the winning state by adding a move
            j = 1
            while i+j**2 <= n:
                dp[i+j**2] = 1
                j += 1
            
        return dp[n]
