def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # The idea is to use a stack and add all the node on the left of a node first, using a while loop
        snode = []
        curr = root
        ans = []
        while curr or snode:
            while curr:
                snode.append(curr)
                curr = curr.left
                
            # When there is no node left to traverse, pop the current node (which is the left most child)
            curr = snode.pop()
            ans.append(curr.val)
            
            # Traverse on the right branch of the tree
            curr = curr.right
            
        return ans
