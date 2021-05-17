def minCameraCover(self, root: TreeNode) -> int:
        self.res = 0
        def DFS(root):
            # Return 2 if this node is covered
            if not root: return 2
            l, r = DFS(root.left), DFS(root.right)
            
            # Return 0 if this node is a not yet covered
            # Being greedy, we will alway put the camera at the parent of this node
            if l == 0 or r == 0:
                self.res += 1
                # Return 1 if we placed a camera here
                return 1
            return 2 if l == 1 or r == 1 else 0
        
        # Need to handle the base case where root is None
        return (DFS(root)==0) + self.res
