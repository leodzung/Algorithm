class Solution(object):
    def __init__(self):
        # To find cycle in the graph
        self.rank = {}
        # The graph itself
        self.graph = defaultdict(list)
        # The connection map. To return the result after removing edges in all cycles
        self.cmap = {}
        
    def criticalConnections(self, n, connections):
        self.formGraph(n, connections)
        self.DFS(0, 0)

        result = []
        for u, v in self.cmap:
            result.append([u, v])

        return result
        
    # Construct the graph        
    def formGraph(self, n, connections):
        self.__init__()
        for i in range(n):
            self.rank[i] = None
            
        for u, v in connections:
            self.graph[u].append(v)
            self.graph[v].append(u)
            
            self.cmap[(min(u, v), max(u, v))] = True
            
    # Recursively traverse the graph to find cycle, and return the minimum rank of the current traversal            
    def DFS(self, node, discovery_rank):
        # If we already seen this node and rank it, return the rank
        if self.rank[node]:
            return self.rank[node]
        
        # Otherwise, assign it to discovery_rank
        self.rank[node] = discovery_rank
        
        # Current min rank
        min_rank = discovery_rank + 1
        
        # Start traversing
        for nbor in self.graph[node]:
            # If this is the parent node (the node we start DFS with), skip it
            if self.rank[nbor] and self.rank[nbor] == discovery_rank - 1:
                continue
                
            recursive_rank = self.DFS(nbor, discovery_rank+1)
            
            # If we found a node with lower rank, this shows that it is part of a cycle
            if recursive_rank <= discovery_rank:
                # Delete the this edge
                del self.cmap[(min(node, nbor), max(node, nbor))]
                
            min_rank = min(min_rank, recursive_rank)
            
        return min_rank
