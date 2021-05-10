from heapq import heapify, heapreplace

class Solution(object):
    def isPossible(self, target):
        """
        :type target: List[int]
        :rtype: bool
        """
        # Keep track of the current sum
        s = sum(target)
        
        # Max heap
        neg = [-num for num in target]
        heapify(neg)
        
        while -neg[0] > 1:
            # Sum of the array without the largest
            remain = s+neg[0]
            
            if remain <= 0:
                return False
            # If the largest is bigger than sum of the rest, 
            # we will keep subtracting the rest from the largest
            # Therefore, we only need the remainder. Replace it with the largest
            elif -neg[0] > remain:
                s = remain + (-neg[0] % remain)
                heapreplace(neg, -(-neg[0] % remain))
            elif -neg[0] != 1:
                return False
        
        return True
