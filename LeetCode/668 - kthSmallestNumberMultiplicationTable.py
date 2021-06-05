# Note that the reverse problem is easier to solve: 
# Given number x, we can find its place in the sorted table
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        # Make sure n >= m
        m, n = min(m, n), max(m, n)
        
        # Check if x at least larger than k numbers in the table
        def enough(x):
            count = 0
            for i in range(1, m+1):
                count += min(x//i, n)
            
            # Count is the position of x in the sorted table
            return count >= k
        
        # Binary search
        lo, hi = 1, m*n
        while lo < hi:
            mi = (lo+hi) // 2
            if not enough(mi):
                lo = mi + 1
            else:
                hi = mi
                
        return lo
