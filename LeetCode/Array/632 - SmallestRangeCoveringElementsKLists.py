def smallestRange(self, nums: List[List[int]]) -> List[int]:
        K = len(nums)
        
        # This is to count the appearance of array elements
        seen = {}
        
        # This is to combine all the numbers from all the arrays
        allNums = []
        for i, nlist in enumerate(nums):
            seen[i] = 0
            for num in nlist:
                allNums.append((num, i))
                
        # Sort the array by its number value
        allNums.sort(key=lambda x:x[0])

        # Maximum length
        length = 2*10**5+1
        ans = None
        begin = 0
        
        # We start from K and count down to 0
        count = K
        
        # We search for the first range that includes elements from all arrays
        for end in range(len(allNums)):
            evalue, eindex = allNums[end]
            
            # If we haven't seen this array index before, we decrease the count because we have an element from a new array
            if seen[eindex] == 0:
                count -= 1
                
            # Increase the count of the current index
            seen[eindex] += 1
            
            # If the count reaches 0, it means that we have the elements from each array
            while count == 0:
                # Start calculating the range
                bvalue, bindex = allNums[begin]
                if evalue - bvalue < length:
                    length = evalue - bvalue
                    ans = [bvalue, evalue]
                    
                # We remove the beginning element, thus we need to increase the count
                if seen[bindex] == 1:
                    count += 1
                    
                # Decrease the count for the beginning index
                seen[bindex] -= 1
                begin += 1
                
        return ans
