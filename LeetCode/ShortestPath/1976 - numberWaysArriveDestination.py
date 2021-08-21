def countPaths(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        graph = defaultdict(list)
        for u, v, l in roads:
            graph[u].append((v, l))
            graph[v].append((u, l))
            
        # Shortest distances from source 0 to current intersection
        dist = [float('inf')] * n
        dist[0] = 0
        
        # Number of shortest paths to current intersection
        count = [0] * n
        count[0] = 1
        
        # Djikstra
        heap = [(0, 0)]
        while heap:
            min_dist, inter = heappop(heap)
            # Found last intersection, stop as this is the minimum distance
            if inter == n-1:
                return count[inter] % (10**9+7)
            
            # Otherwise, process each neighbors of the current intersection
            for neigh, length in graph[inter]:
                distance = min_dist + length
                # If the current distance is the same with the minimum distance at this intersection
                # It means that we reached this intersection from other way
                if distance == dist[neigh]:
                    count[neigh] += count[inter]
                # If this current distance is the new minimium, update dist, count, and heap
                elif distance < dist[neigh]:
                    dist[neigh] = distance
                    count[neigh] = count[inter]
                    heappush(heap, (distance, neigh))
