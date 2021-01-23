def lcaDeepestLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # The idea is to traverse the tree twice.
        # The first time to to annotate the tree with each node's depth, and find the depth of the leaves
        self.depth = 0
        self.nmap = {}
        
        # Preorder traverse
        def dfs(node, level):
            if node:
                dfs(node.left, level+1)
                dfs(node.right, level+1)
                    
                # Keep track of the deepest level
                if self.depth < level:
                    self.depth = level
                    
                # Use map to keep track of the level of each node
                self.nmap[node] = level
                        
        dfs(root, 0)
        
        # Recursively traverse the tree to find the deepest ancestor
        def findCommonAncester(node):
            # If node is None return None. 
            # If node is one of the deepest node, mark it as the deepest
            if not node or self.nmap[node] == self.depth:
                return node
            
            # Recursively traverse the left subtree and right subtree to find the nodes that are marked as the deepest
            left = findCommonAncester(node.left)
            right = findCommonAncester(node.right)
            
            # If we find marked nodes in both left tree and right tree, it mean that our current node is the common ancestor
            # If only find marked node in the left or the right tree, return it instead
            return node if left and right else left or right
        
        return findCommonAncester(root)
