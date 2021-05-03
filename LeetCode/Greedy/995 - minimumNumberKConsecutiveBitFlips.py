def minKBitFlips(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        N = len(A)
        # This mark the closing of the windows
        # Note that this mark can be flipped as well if it is inside other flipping windows
        closing = [0] * N
        ans = flip = 0
        
        for i, x in enumerate(A):
            # Decide do we need to flip at the current position
            flip ^= closing[i]
            # If we do need to flip
            if x ^ flip == 0:
                ans += 1
                # If the current window expands beyond the array, we cannot flip it
                if i+K > N:
                    return -1
                # Mark this window as currently being flipped
                flip ^= 1
                
                # Mark the end of the window
                if i+K < N:
                    closing[i+K] ^= 1
                    
        return ans
