class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        # Incs is to count all the numbers that divisible by num (increment of num)
        # For example, if max(nums) = 9, and 2 is in nums, we will have [0, 0, 1, 0, 1, 0, 1, 0, 1, 0]
        # There are 4 numbers that are multipliers of 2, and so 9//2 = 4
        incs, counter = [0]*(max(nums)+1), Counter(nums)
        
        for num in counter:
            for j in range(num, len(incs), num):
                incs[j] += counter[num]
                
        quats = list(accumulate(incs))
        return sum([quats[num] for num in nums]) % 1_000_000_007
