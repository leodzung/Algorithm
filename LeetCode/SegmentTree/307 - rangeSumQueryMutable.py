class NumArray(object):

    def __init__(self, nums):
        self.N = len(nums)
        self.tree = self.buildTree(nums)
        
    def buildTree(self, nums):
        tree = [0 if i < self.N else nums[i-self.N] for i in range(2*self.N)]
        
        # Build parent nodes
        for i in range(self.N-1, -1, -1):
            tree[i] = tree[i*2] + tree[i*2+1]
            
        return tree

    def update(self, index, val):
        index += self.N
        self.tree[index] = val
        
        # Update ancestors of the impacted node
        while index:
            left = right = index
            # Find the correct left (or right) node
            if index%2:
                left = index-1
            else:
                right = index+1
                
            # Update parent node and repeat
            self.tree[index//2] = self.tree[left] + self.tree[right]
            index //= 2

    def sumRange(self, left, right):
        left += self.N
        right += self.N
        
        ans = 0
        while left <= right:
            # Left is the right child of its parent, which is outside of the range [left, right]
            # Therefore we need to add the left node, because its parent won't be count
            if left%2:
                ans += self.tree[left]
                left += 1
                
            # Right is the left child of its parent, which is outside of the range [left, right]
            # Therefore we need to add the right node, because its parent won't be count
            if right%2 == 0:
                ans += self.tree[right]
                right -= 1
                
            # Otherwise, the parents will be included in the range [left, right]
            left //= 2
            right //= 2
            
        return ans
