class DSU(object):
    def __init__(self):
        self.parent = list(range(10001))
        self.rank = [0] * 10001
       
    # Path compression
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
            
        return self.parent[x]
    
    # Union find by rank
    def union(self, x, y):
        if self.rank[x] <= self.rank[y]:
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1
            self.parent[self.find(x)] = self.find(y)
        elif self.rank[y] < self.rank[x]:
            self.parent[self.find(y)] = self.find(x)
        
        
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dsu = DSU()
        
        # Mapping email to id, id to email, and id to name
        emap, idmap, nmap = {}, {}, defaultdict(str)
        
        # To generate unique IDs
        self.curId = 0
                       
        # Get ID from an email
        def getId(email):
            if email not in emap:
                emap[email] = self.curId
                idmap[self.curId] = email
                self.curId += 1
                
            return emap[email]
            
        for account in accounts:
            name, emails = account[0], account[1:]
            
            # Union all the emails from the same account
            emailId = getId(emails[0])
            nmap[emailId] = name
            for i in range(1, len(emails)):
                id = getId(emails[i])
                dsu.union(emailId, id)
                nmap[id] = name
                
        ans = defaultdict(list)
        for email in emap.keys():
            # Find the leader (parent) and use it as key
            ans[dsu.find(emap[email])].append(email)
            
        return [[nmap[id]] + sorted(ans[id]) for id in ans.keys()]
