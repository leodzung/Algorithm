class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        N = len(prices)
        rest = [0] * N
        hold = [0] * N
        sell = [0] * N
        
        hold[0] = -prices[0]
        
        for i in range(1, N):
            # Just sold or continue to rest
            rest[i] = max(rest[i-1], sell[i-1])
            # Just bought or continue to hold
            hold[i] = max(hold[i-1], rest[i-1]-prices[i])
            # Update sell if needed be (to update rest state)
            sell[i] = max(sell[i-1], hold[i-1]+prices[i])
            
        # Last state can be resting or selling
        return max(rest[-1], sell[-1])
