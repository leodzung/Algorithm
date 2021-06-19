def bestRotation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        bad = [0] * N
        for i, num in enumerate(nums):
            # The left and right boundaries of the bad interval
            # Meaning if we shift any k in the interval, the current entry will not get any score
            left, right = (i-num+1)%N, (i+1)%N
            # Mark the interval by cummulative
            bad[left] -= 1
            bad[right] += 1
            
            # If this is a wrap-around interval
            if left > right:
                bad[0] -= 1
                
        best = -N
        ans = cur = 0
        for i, score in enumerate(bad):
            cur += score
            if cur > best:
                best = cur
                ans = i
                
        return ans
