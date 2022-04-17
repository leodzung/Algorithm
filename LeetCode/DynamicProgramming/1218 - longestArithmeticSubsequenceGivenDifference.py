def longestSubsequence(self, arr: List[int], difference: int) -> int:
        # Space: O(N)
        lengthMap = defaultdict(int)
        
        # Time: O(N)
        for num in arr:
            lengthMap[num] = max(lengthMap[num], lengthMap[num-difference] + 1)
            
        return max(lengthMap.values())
