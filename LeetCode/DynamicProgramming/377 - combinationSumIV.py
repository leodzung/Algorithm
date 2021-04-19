class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0] * (target+1)
        dp[0] = 1
        
        for csum in range(target+1):
            for num in nums:
                # When current sum and current number add up to target, we found a 
                # new connection from previous set (target-num), each added up to target. 
                # We need to add this set to the result set
                if csum+num < target+1:
                    dp[csum+num] += dp[csum]
        
        return dp[target]
