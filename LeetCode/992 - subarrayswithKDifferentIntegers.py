class Window:
    def __init__(self):
        self.count = Counter()
        # Count (non-zero) unique numbers in counter
        self.nonzero = 0
        
    def add(self, x):
        self.count[x] += 1
        if self.count[x] == 1:
            self.nonzero += 1
            
    def remove(self, x):
        self.count[x] -= 1
        if self.count[x] == 0:
            self.nonzero -= 1

class Solution(object):
    def subarraysWithKDistinct(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        # Window1 to keep track of the longest good sub-array
        # Window2 to keep track of the sub-array that if we add 1 more number, we will have a good sub-array
        window1, window2 = Window(), Window()
        
        ans = 0
        left1 = left2 = 0
        for right, x in enumerate(A):
            window1.add(x)
            window2.add(x)
            
            while window1.nonzero > K:
                window1.remove(A[left1])
                left1 += 1
                
            while window2.nonzero >= K:
                window2.remove(A[left2])
                left2 += 1
            
            # Any array in between window1 and window2 will the a good sub-array
            ans += left2 - left1
            
        return ans
