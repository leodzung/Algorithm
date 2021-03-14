# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.foundP = False
        self.foundQ = False
        
        self.pathP = []
        self.pathQ = []
        
        def explore(node, path):
            # print(node, path)
            if not node:
                return
            
            if not (self.foundQ and self.foundP):
                path.append(node)
                
                if node == p:
                    # print(node, path)
                    self.foundP = True
                    self.pathP = list(path)
                elif node == q:
                    # print(node, path)
                    self.foundQ = True
                    self.pathQ = list(path)
                
                explore(node.left, list(path))
                explore(node.right, list(path))
                    
        explore(root, [])
        
        # print(self.pathP)
        # print(self.pathQ)    
        
        for i in range(min(len(self.pathP), len(self.pathQ))):
            if self.pathP[i].val != self.pathQ[i].val:
                return self.pathP[i - 1]
        
        return self.pathP[i]
