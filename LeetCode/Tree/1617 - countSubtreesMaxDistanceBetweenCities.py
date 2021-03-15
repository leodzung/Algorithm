def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        def BFS(source, cities):
            seen = {source}
            q = deque([(source, 0)])
            farthestNode, farthestDist = -1, 0
            while q:
                farthestNode, farthestDist = u, d = q.popleft()
                for v in graph[u]:
                    if v not in seen and v in cities:
                        seen.add(v)
                        q.append((v, d+1))
                        
            return farthestNode, farthestDist, seen
        
        # Calculate diameter for a set of cities
        def diameter(cities):
            # Start BFS from any city
            source = cities.pop()
            cities.add(source)
            farthestNode, _, seen = BFS(source, cities)
            
            # If we cannot explore all the cities from the source, it mean the cities are not connected
            if len(seen) < len(cities):
                return 0
            
            # Otherwise, BFS from ther farthestNode to get the diameter
            _, dist, _ = BFS(farthestNode, cities)
            return dist
        
        # Calculate max distance for a state
        def maxDistance(state):
            cities = set()
            
            # Decide which cities will be included in this state
            for i in range(n):
                if (state >> i) & 1 == 1:
                    cities.add(i)
                    
            return diameter(cities)
                        
        # Create the graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u-1].append(v-1)
            graph[v-1].append(u-1)
            
        ans = [0] * (n-1)
        
        # Generate 2^n state
        for state in range(1, 2**n):
            d = maxDistance(state)
            if d > 0:
                ans[d-1] += 1
                
        return ans
