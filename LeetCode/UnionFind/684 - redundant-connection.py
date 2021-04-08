class DSU(object):
    def __init__(self):
        # Size of node is less than 1000
        self.parent = list(range(1001))
        self.rank = [0] * 1001
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
            
        return self.parent[x]
    
    # Union by rank, which gurantee that after each operation, the number of disjointed components reduced by at least half
    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        elif self.rank[xr] < self.rank[yr]:
            self.parent[xr] = yr
        elif self.rank[yr] > self.rank[xr]:
            self.parent[yr] = xr
        else:
            self.parent[yr] = xr
            self.rank[xr] += 1
            
        return True
        

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU()
        
        for edge in edges:
            if not dsu.union(*edge):
                return edge
