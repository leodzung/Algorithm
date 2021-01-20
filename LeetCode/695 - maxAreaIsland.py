class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        
        self.visited = [[0] * n for _ in range(m)]
        # print(self.visited)
        ans = []
        
        def cal(row, col):
            self.visited[row][col] = 1
            ans = 1
            
            if row > 0 and grid[row-1][col] and not self.visited[row-1][col]:
                ans += cal(row-1, col)
            if row < m-1 and grid[row+1][col] and not self.visited[row+1][col]:
                ans += cal(row+1, col)
            
            if col > 0 and grid[row][col-1] and not self.visited[row][col-1]:
                ans += cal(row, col-1)
            if col < n-1 and grid[row][col+1] and not self.visited[row][col+1]:
                ans += cal(row, col+1)
                
            # print(row, col, ans)
            return ans
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    area = cal(i, j)
                    ans.append(area)
        
        # print(self.ans)
        # print(self.visited)
        if not ans:
            return 0
        
        return max(ans)
