from heapq import heapify, heappush, heappop

class Solution(object):
    def assignTasks(self, servers, tasks):
        """
        :type servers: List[int]
        :type tasks: List[int]
        :rtype: List[int]
        """
        available = [(weight, index) for index, weight in enumerate(servers)]
        heapify(available)
        
        ans = [-1] * len(tasks)
        occupied = []
        
        # Current time
        t = 0
        for i, time in enumerate(tasks):
            # If we have to wait because there are no server available, t might already bigger than i
            t = max(i, t)
            # No server available. Need to update t to the nearest future time when first server is available
            if not available:
                t = occupied[0][0]
            
            # Free up occupied servers if the tasks are done
            while occupied and t >= occupied[0][0]:
                _, server = heappop(occupied)
                heappush(available, (server))
            
            # Processing new task
            weight, index = heappop(available)
            ans[i] = index
            # Push COMPLETION time and server to the occupied list
            heappush(occupied, (t+time, (weight, index)))

        return ans    
