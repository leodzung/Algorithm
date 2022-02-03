def rob(self, root: Optional[TreeNode]) -> int:
        def postorder(node):
            # Rob children, Rob self
            if not node:
                return 0, 0
            
            l = postorder(node.left)
            r = postorder(node.right)
            
            return max(l)+max(r), node.val+l[0]+r[0]
        
        # print(postorder(root))
        return max(postorder(root))
