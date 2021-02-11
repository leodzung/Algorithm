def makeLargestSpecial(self, S: str) -> str:
        """
        Observation: all the special binary strings start with 1 and end with 0
        Therefore, we can recurse on the string in between 1 and 0 to generate all possible special strings
        Then we sort the special string to rebuild the lexicographically largest string
        """
        # Keep track of the difference between the numbers of 1 and 0
        count = 0
        
        current_index = 0
        
        # Keep track of all special sub strings
        ans = []
        for i in range(len(S)):
            # Increase the count if we see a 1 and decrease it if we see a 0
            count = count+1 if S[i] == '1' else count-1
            
            # If the number of 1 equal the number of 0, this is a special string
            if count == 0:
                # Recurse with the string in between
                ans.append('1' + self.makeLargestSpecial(S[current_index+1:i]) + '0')
                # Update current index
                current_index = i+1
                
        ans.sort(reverse=True)
        # print(ans)
        return ''.join(ans)
