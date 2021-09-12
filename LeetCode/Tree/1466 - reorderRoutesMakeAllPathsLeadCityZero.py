class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        outgoing = defaultdict(list)
        incoming = defaultdict(list)
        
        for source, end in connections:
            outgoing[source].append(end)
            incoming[end].append(source)
            
        seen = set()
        seen.add(0)
        
        ans = 0
        # Safe cities
        ins = [0]
        # Non-safe, neighboring cities
        outs = []
        
        while ins:
            node = ins.pop()
            
            for neigh in incoming[node]:
                if neigh not in seen:
                    seen.add(neigh)
                    ins.append(neigh)
                    
            for neigh in outgoing[node]:
                if neigh not in seen:
                    seen.add(neigh)
                    outs.append(neigh)
                    
            if not ins and outs:
                ins.append(outs.pop())
                ans += 1
                        
        return ans      
