class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Dimensions of grid
        m, n = len(grid), len(grid[0])
        
        # 4-directional walks
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        start = end = None
        
        # Map to track the neighbors for the start cell and empty cells
        nmap = {}
        
        # Find the start and end cells and initiate the set to keep track of those cell's neighbors
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start = (i, j)
                    nmap[start] = set()
                elif grid[i][j] == 2:
                    end = (i, j)
                elif grid[i][j] == 0:
                    nmap[(i, j)] = set()
                    
        # Add neighbors to the created sets
        for x, y in nmap:
            for dx, dy in moves:
                if(x+dx, y+dy) in nmap:
                    nmap[(x, y)].add((x+dx, y+dy))
                 
        # Create a set for backtracking
        visited = set([start])
        # print(visited)
        
        # This is to check whether we have reached destination
        last_cells = set((end[0]+dx, end[1]+dy) for (dx, dy) in moves)
        # print(last_cells)
        
        # Function to backtrack from a cell
        def backtrack(cell):
            # Check how many cells left to visit before reaching the end
            left_to_visit = len(nmap) - len(visited)
            
            # Note that the end cell is not on the list of neighbors, so it is unreachable
            # Backtrack thus ends when reaching one of the the last_cells, which is right next to the end cell
            if not left_to_visit:
                # print(int(cell in last_cells))
                return int(cell in last_cells)
            
            ans = 0
            for neighbor in (nmap[cell] - visited):
                visited.add(neighbor)
                ans += backtrack(neighbor)
                visited.remove(neighbor)
            
            return ans
        
        # Backtrack from the start cell
        return backtrack(start)
