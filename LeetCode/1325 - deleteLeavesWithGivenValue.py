def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        # Idea is to use DFS to remove all the leaves first
        # The resulting leaves will be handled by recursive calls
        
        # We keep track of the parent to remove the node when needed
        # Also keep track of whether it is the left or right node
        def DFS(node, parent, left):
            if node:
                if node.left:
                    DFS(node.left, node, True)
                if node.right:
                    DFS(node.right, node, False)
                    
                if not node.left and not node.right and node.val == target:
                    # Remove the node
                    if left:
                        parent.left = None
                    else:
                        parent.right = None
        
        # Create a parent node for root in case we need to remove root
        parent = TreeNode(left=root)
        DFS(root, parent, True)
        
        return parent.left
