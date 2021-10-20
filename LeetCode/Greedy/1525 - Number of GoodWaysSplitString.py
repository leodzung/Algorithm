class Solution(object):
    def getMinSwaps(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: int
        """
        n = len(num)
        
        # Get the next wonderful integer
        def getNext(num):
            # Find the first number of the right that is less than the next one
            i = n-1
            while num[i] <= num[i-1]:
                i -= 1
            j = i
            # Find the smallest number to the right of and bigger than the number above to swap
            # Note that the numbers on the right of the first number are in descending order
            while j < n and num[i-1] < num[j]:
                j += 1
            num[i-1], num[j-1] = num[j-1], num[i-1]
            
            # Since the tail after swapping is in descending order, reverse to make it smallest
            num[i:] = num[i:][::-1]
            return num
        
        new_num = list(num)
        num = list(num)
        
        for _ in range(k):
            new_num = getNext(new_num)
            
        ans = 0
        for i in range(n):
            # If the two numbers at the same index differ, count the number of swaps to reconcile
            j = i
            while j < n and new_num[i] != num[j]:
                j += 1
            
            ans += j-i
            num[i:j+1] = [num[j]] + num[i:j]
            
        return ans     
