def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        R, C = len(matrix), len(matrix[0])
        
        # Generate neighbors
        def neighbors(r, c):
            for newr, newc in ((r+1, c), (r-1, c), (r, c-1), (r, c+1)):
                if 0 <= newr < R and 0 <= newc < C and matrix[newr][newc] > matrix[r][c]:
                    yield newr, newc
                
        # Track longest path starting from a cell                
        pmap = defaultdict(int)
        self.ans = 0
        
        # Explore from cell
        def explore(r, c):
            # If we already seen this cell from recursion
            if (r, c) in pmap:
                return pmap[r, c]
            
            path = 1
            for row, col in neighbors(r, c):
                if (row, col) not in pmap:
                    pmap[row, col] = explore(row, col)
                    
                path = max(path, pmap[row, col]+1)
                
            self.ans = max(self.ans, path)
            pmap[r, c] = path
            return path
                
        for r in range(R):
            for c in range(C):
                    explore(r, c)
                
        return self.ans
