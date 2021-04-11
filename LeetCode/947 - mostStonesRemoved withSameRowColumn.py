class DSU(object):
    def __init__(self):
        self.parent = list(range(1001))
        self.rank = [0] * 1001
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]
    
    def union(self, x, y):
        if self.rank[x] <= self.rank[y]:
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1
            self.parent[self.find(x)] = self.find(y)
        else:
            self.parent[self.find(y)] = self.find(x)

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        idmap = defaultdict(int)
        self.id = 0
        
        def getId(stone):
            if (stone[0], stone[1]) not in idmap:
                idmap[(stone[0], stone[1])] = self.id
                self.id += 1
                
            return idmap[(stone[0], stone[1])]
            
        dsu = DSU()
        N = len(stones)
        for i in range(N-1):
            for j in range(i+1, N):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    # print(stones[i], stones[j])
                    dsu.union(getId(stones[i]), getId(stones[j]))
             
        # print(idmap)
        cmap = defaultdict(int)
        for x, y in stones:
            if (x, y) in idmap:
                cmap[dsu.find(idmap[x, y])] += 1
            
        # print(cmap)
            
        ans = 0
        for val in cmap.values():
            ans += val-1

        return ans
