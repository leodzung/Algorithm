def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)
        
        def neighbors(row, col):
            for nrow, ncol in ((row-1, col), (row+1, col), (row, col-1), (row, col+1)):
                if 0 <= nrow < N and 0 <= ncol < N:
                    yield nrow, ncol
                    
        def DFS(row, col, index):
            area = 1
            grid[row][col] = index
            for nrow, ncol in neighbors(row, col):
                if grid[nrow][ncol] == 1:
                    area += DFS(nrow, ncol, index)
                    
            return area
        
        area = {}
        # Start at 2 because the matrix comprises of 0s and 1s and we don't want to mix up
        index = 2
        
        # Caculate largest island areas
        for row in range(N):
            for col in range(N):
                if grid[row][col] == 1:
                    area[index] = DFS(row, col, index)
                    index += 1
                    
        ans = max(area.values() or [0])
        
        # Merging 0 with the surrounding areas
        for row in range(N):
            for col in range(N):
                if grid[row][col] == 0:
                    # Set of neighboring areas that current 0 sees
                    seen = {grid[nrow][ncol] for nrow, ncol in neighbors(row, col) if grid[nrow][ncol] > 1}
                    ans = max(ans, 1+sum(area[i] for i in seen))
                    
        return ans
