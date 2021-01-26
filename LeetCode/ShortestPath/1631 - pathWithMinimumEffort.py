from heapq import heappush, heappop
import math

class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        if not heights:
            return 0
        
        row, col = len(heights), len(heights[0])
        heap = [(0, (0, 0))]
        
        # Keep track of the cost of current (row, col)
        # Also can use it to keep track of whether we visited (row, col)
        currentCost = {(0,0): 0}
        
        # All possible moves
        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        target = (row-1, col-1)
        
        # Processing the heap
        while heap:
            cost, (x, y) = heappop(heap)
            # print(cost, x, y)
            
            # We stop calculating cost after reaching target
            if (x, y) == target:
                break
                
            # Try each move
            for (dx, dy) in moves:
                newX, newY = x+dx, y+dy
                
                # If the move is valid, ie. inside of the grid
                if 0 <= newX < row and 0 <= newY < col:
                    newCost = max(cost, abs(heights[x][y] - heights[newX][newY]))
                    
                    # If we haven't reach this point or we have a better cost, update heap
                    if (newX, newY) not in currentCost or newCost<currentCost[(newX, newY)]:
                        currentCost[(newX, newY)] = newCost
                        heappush(heap, (newCost, (newX, newY)))
                        
        return currentCost[target]
        
