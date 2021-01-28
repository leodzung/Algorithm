def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        # Calculate sum of the path up until the current node
        def helper(node):
            if not node:
                return 0
            
            left = helper(node.left) + node.val
            right = helper(node.right) + node.val
            # print(left, right)
            
            # We have to subtract the node.val because both the left and right paths include the value of the current node
            self.ans = max(self.ans, left+right-node.val, left, right)
            
            # We have to include 0 to account for the scenario when left, right, and node.val are negative.
            # In such scenario, we simply ignore the current node by settting the max value to 0
            # Example [-3]
            return max(left, right, 0, node.val)
        
        self.ans = root.val
        helper(root)
        
        return self.ans
