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
        for freq, token in (-a, "a"), (-b, "b"), (-c, "c"):
            if freq:
                heappush(heap, (freq, token))
        
        ans = ""
        while heap:
            # Get the token with the most remaining number
            fchar1, char1 = heappop(heap)
            # If it is the same with the last two characters in the current answer
            # Means that we ran out of other two tokens
            if len(ans) > 1 and ans[-1] == ans[-2] == char1:
                return ans
            
            # Being greedy, we take 2 of the most available token if possible
            # Which is when it has at least 2 availabe and it is not the same as the last character
            if fchar1 < -2 and (not ans or ans[-1] != char1):
                ans += 2*char1
                fchar1 += 2
            # Otherwise, we will have to take only one instance of the most available token
            else:
                ans += char1
                fchar1 += 1
                
            # If other token(s) are available
            # We will use the second most available token to separate the most available token above
            if heap:
                fchar2, char2 = heappop(heap)
                
                # We need just 1 instance of the second most available token to separate
                ans += char2
                fchar2 += 1
                # Add back the second most available token if it is still available
                if fchar2 < 0:
                    heappush(heap, (fchar2, char2))
                        
            # Add back the most available token if it is still available
            if fchar1 < 0:
                heappush(heap, (fchar1, char1))
                    
        return ans     
