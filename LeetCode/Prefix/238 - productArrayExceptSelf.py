def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        ans = []
        
        # Calculate prefix products before the interested elements
        p = 1
        for i in range(N):
            ans.append(p)
            p *= nums[i]
        print(ans)
        
        # Calculate the suffix products after the interested elements
        p = 1
        for i in range(N-1, -1, -1):
            # Product of prefix - ans, and suffix - p
            ans[i] *= p
            p *= nums[i]
            
        return ans
