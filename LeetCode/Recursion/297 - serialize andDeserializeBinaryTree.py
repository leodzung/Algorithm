class Codec:
    def serialize(self, root):
        """
        Encode as a preorder traversal
        
        :type root: TreeNode
        :rtype: str
        """
        ans = []
        
        def preorder(node):
            if node:
                ans.append(node.val)
            
                preorder(node.left)
                preorder(node.right)
            else:
                ans.append(None)

        preorder(root)
        
        return ans

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # print(data)
        if data[0] == None:
            data.pop(0)
            return None

        root = TreeNode(data[0])
        data.pop(0)
        root.left = self.deserialize(data)
        root.right = self.deserialize(data)

        return root
