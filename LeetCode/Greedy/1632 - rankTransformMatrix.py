class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        M, N = len(matrix), len(matrix[0])
        ans = [[0]*N for _ in range(M)]
        
        # Map value to its graph. This one will be used later for BFS.
        graphs = {}
        
        # For each value, link all rows and cols
        for r in range(M):
            for c in range(N):
                v = matrix[r][c]
                
                if v not in graphs:
                    graphs[v] = {}
                if r not in graphs[v]:
                    graphs[v][r] = []
                # Columns are represented by complement operation
                # This way we only need to use one graph instead of two
                if ~c not in graphs[v]:
                    graphs[v][~c] = []
                    
                graphs[v][r].append(~c)
                graphs[v][~c].append(r)
        
        # Map value to list of set of connected points
        value2index = defaultdict(list)
        seen = set()
        
        # BFS to link all rows and cols and translate the above graph to set of points
        for r in range(M):
            for c in range(N):
                if (r, c) in seen:
                    continue
                    
                # Haven't seen this point -> start BFS.
                seen.add((r, c))
                v = matrix[r][c]
                graph = graphs[v]
                
                # BFS
                q = [r, ~c]
                # Set of connected rows and cols
                rowcols = {r, ~c}
                while q:
                    node = q.pop(0)
                    for rowcol in graph[node]:
                        if rowcol not in rowcols:
                            q.append(rowcol)
                            rowcols.add(rowcol)
                   
                # Set of connected point
                points = set()
                for rowcol in rowcols:
                    for k in graph[rowcol]:
                        # K is row
                        if k >= 0:
                            points.add((k, ~rowcol))
                            seen.add((k, ~rowcol))
                        # K is col
                        else:
                            points.add((rowcol, ~k))
                            seen.add((rowcol, ~k))
                            
                value2index[v].append(points)
              
        # Keep track of the current maxima of each row and column in current answer matrix
        rowmax = [0] * M
        colmax = [0] * N
        for v in sorted(value2index.keys()):
            # Calculate each set of points independently
            for points in value2index[v]:
                rank = 1
                for r, c in points:
                    rank = max(rank, max(rowmax[r], colmax[c])+1)
                    
                for r, c in points:
                    ans[r][c] = rank
                    # Update current row and col maxima
                    rowmax[r] = max(rowmax[r], rank)
                    colmax[c] = max(colmax[c], rank)
        
        return ans
