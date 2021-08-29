from heapq import heapify, heappush, heappop
class Solution(object):
    def longestDiverseString(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: str
        """
        heap = []
        if a:
            heappush(heap, (-a, "a"))
        if b:
            heappush(heap, (-b, "b"))
        if c:
            heappush(heap, (-c, "c"))
        
        ans = ""
        while heap:
            fchar1, char1 = heappop(heap)
            
            # "####bb" b=3 a=0 c=0
            if len(ans) > 1 and ans[-1] == ans[-2] == char1:
                return ans
            
            # a = 8
            # "bba" cannot add "aa" -> "bbaab"
            if fchar1 < -2 and (not ans or ans[-1] != char1):
                ans += 2*char1
                fchar1 += 2
            else:
                ans += char1
                fchar1 += 1
                
            if heap:
                fchar2, char2 = heappop(heap)
                
                if fchar2 <= -1:
                    ans += char2
                    fchar2 += 1
                    if fchar2 < 0:
                        heappush(heap, (fchar2, char2))
                        
            if fchar1 < 0:
                heappush(heap, (fchar1, char1))
                    
        return ans     
