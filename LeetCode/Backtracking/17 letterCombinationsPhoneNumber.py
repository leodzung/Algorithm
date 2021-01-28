def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # Handle edge case when digits is empty
        n = len(digits)
        if not n:
            return []
        
        # Create a digit map
        dmap = {2:['a', 'b', 'c'], 3:['d', 'e', 'f'], 4:['g', 'h', 'i'], 5:['j', 'k', 'l'], 6:['m', 'n', 'o'], 7:['p', 'q', 'r', 's'], 8:['t', 'u', 'v'], 9:['w', 'x', 'y', 'z']}
        # print(dmap)
        
        self.ans = []
        def backtrack(comb, pos):
            # If length of the combination the same with digits', append it to the result array
            if len(comb) == n:
                self.ans.append(comb)
                return
            
            for index in range(pos, n):
                # Get the available characters of the current digit
                chars = dmap[int(digits[index])]
                # print(chars)
                
                for char in chars:
                    # print(char)
                    comb += char
                    backtrack(comb, index+1)
                    # Remove the last added character to backtrack
                    comb = comb[:len(comb)-1]
                    # print(comb)
        
        backtrack("", 0)
        
        return self.ans
