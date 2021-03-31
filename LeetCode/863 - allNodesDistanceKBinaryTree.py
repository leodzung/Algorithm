class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        if K == 0:
            return [target.val]
        
        pmap = {}
        def DFS(node):
            if node:
                if node.left:
                    pmap[node.left] = node
                    DFS(node.left)
                if node.right:
                    pmap[node.right] = node
                    DFS(node.right)
                
        DFS(root)
        # print(pmap)
        
        nset = set()
        seen = set()
        # Find all CHILD nodes from parent. Example: find(5, 2) return [7, 4]
        def find(node, distance):
            # print(node.val, distance)
            if distance == 0 and node:
                nset.add(node.val)
                return
                    
            if node:
                if node.left and node.left not in seen:
                    seen.add(node.left)
                    find(node.left, distance-1)
                if node.right and node.right not in seen:
                    seen.add(node.right)
                    find(node.right, distance-1)
                
                if node in pmap and pmap[node] not in seen:
                    seen.add(pmap[node])
                    find(pmap[node], distance-1)
                
        seen.add(target)
        find(target, K)
        return list(nset)
