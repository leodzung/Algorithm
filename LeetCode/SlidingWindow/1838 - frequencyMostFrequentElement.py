def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        N = len(nums)
        ans = 1
        # Sliding window from left to right
        left = right = 0
        s = 0
        nums.sort()
        
        while right < N:
            # Keep adding number to the right to maximize the current windows
            s += nums[right]
            
            # Adding k to the current sum is not enough to expand the windows
            # It means we have maximized the current windows -> time to move the left pointer
            while (s+k < nums[right] * (right-left+1)):
                s -= nums[left]
                left += 1
            
            # Record the current maximized window
            ans = max(ans, right-left+1)
            right += 1
            
        return ans
