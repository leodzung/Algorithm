from collections import defaultdict
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        # Matrix dimentions
        r, c = len(matrix), len(matrix[0])
        
        # Create a prefix sum matrix to calculate sum up until the current element (r, c)
        prefix_sum = [[0] * (c+1) for _ in range(r+1)]
        # print(prefix_sum)
        
        for i in range(1, r+1):
            for j in range(1, c+1):
                prefix_sum[i][j] = prefix_sum[i-1][j] + sum(matrix[i-1][:j])
                
        ans = 0
        
        # We fix two rows r1 and r2 and calculate the sum of all the rectangles that are bound by r1 and r2
        for r1 in range(1, r+1):
            for r2 in range(r1, r+1):
                # Notice that we have a new dict for each pair of rows (r1, r2)
                # Because the sum of the rectangles with a different pair would not be applicable to the current pair
                nmap = defaultdict(int)
                
                # In case we have a rectangle whose sum is exactly target
                nmap[0] = 1
                
                # Running through the columns
                for col in range(1, c+1):
                    # The cumulative sum of the rectable bounded by r1 and r2 and up until current column
                    s = prefix_sum[r2][col] - prefix_sum[r1-1][col]
                    
                    # Check if we saw s - target before. If yes, it mean currentS - existingS = target -> Rectangle found
                    ans += nmap[s-target]
                    
                    # Register that we have seen the current sum s before
                    nmap[s] += 1
                    
        return ans
