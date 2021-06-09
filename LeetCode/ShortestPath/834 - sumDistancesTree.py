def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
            
        count = [1] * n
        ans = [0] * n
        
        # Calculate the answer for the root, which we assign to the first node
        def BottomUpDFS(node=0, parent=None):
            for child in graph[node]:
                if child != parent:
                    # Postorder DFS to calculate bottom up
                    BottomUpDFS(child, node)
                    count[node] += count[child]
                    ans[node] += ans[child] + count[child]
                    
        # With the correct answer for the root, calculate the answers for its descendants
        def TopDownDFS(node=0, parent=None):
            for child in graph[node]:
                if child != parent:
                    # Preorder DFS to calculate top down
                    ans[child] = (ans[node] - count[child]) + (n - count[child])
                    TopDownDFS(child, node)
                    
        BottomUpDFS()
        TopDownDFS()
        return ans
