def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # left to track the last index of 0 from the left
        # right to track the last index of 1 from the right
        left, right = 0, len(nums)-1
        
        for i in range(len(nums)):
            # This while loop is for when the newly swapped of the current index continue to be 0 or 2
            while i < len(nums) and (nums[i] == 0 or nums[i] == 2) and left < right:
                # print(i, left, right)
                # Swap the current index with the current left index
                if nums[i] == 0 and i > left:
                    nums[i], nums[left] = nums[left], nums[i]
                    left += 1
                    
                # Swap the current index with the current right index
                elif nums[i] == 2 and i < right:
                    nums[i], nums[right] = nums[right], nums[i]
                    right -= 1
                    
                # If the number is not 0 or 2, move on to the next index
                else:
                    i += 1
