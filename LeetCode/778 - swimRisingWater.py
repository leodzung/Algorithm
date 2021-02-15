from heapq import heappush, heapify

class Solution:
    # The idea is to use heap to maintain all the possible moves
    # Because the next move will always be the point with the lowest water level
    def swimInWater(self, grid: List[List[int]]) -> int:
        # Dimensions of the grid
        n = len(grid)
        
        # Map the value with the (row, col)
        wmap = {}
        for i in range(n):
            for j in range(n):
                wmap[grid[i][j]] = (i, j)
                
        # All 4-directional moves        
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # We only push the point that we haven't added to the heap before
        seen = [[0] * n for _ in range(n)]
        
        # Our heap
        wheap = [grid[0][0]]
        heapify(wheap)
        
        start, end = (0, 0), (n-1, n-1)
        # Since we added the first point, we need to mark it as seen
        seen[0][0] = 1
        ans = 0
        
        while wheap:
            # Get the current lowest point from heap
            current = heappop(wheap)
            
            # Update the answer with the water level in the current point
            ans = max(ans, current)
            
            # Get the coordinates of the current point
            row, col = wmap[current]
            
            # If this is the destination, we return the answer
            if (row, col) == end:
                return ans
            
            # Otherwise, try the next move
            for dr, dc in moves:
                # If the next moves are inside the grid, and we haven't seen it before
                if 0 <= row+dr < n and 0 <= col+dc < n and not seen[row+dr][col+dc]:
                    # Mark this new point as seen
                    seen[row+dr][col+dc] = 1
                    # Push it to our heap for next steps
                    heappush(wheap, grid[row+dr][col+dc])
