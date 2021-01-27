def maxScoreWords(self, words, letters, score):
        """
        :type words: List[str]
        :type letters: List[str]
        :type score: List[int]
        :rtype: int
        """
        # Map to keep track of score of each letter
        smap = {}
        for i, s in enumerate(score):
            char = chr(i+ord('a'))
            smap[chr(i+ord('a'))] = s
        
        # Counter to count the number of available letters
        c = Counter()
        for l in letters:
            c[l] += 1
            
        # Calculate the score of each subset            
        def calScore(subset):
            ans = 0
            
            scounter = Counter()
            for word in subset:
                for l in word:
                    scounter[l] += 1
                    
                    # If the number of letter exceeding available letters, the score of the subset will be 0
                    if scounter[l] > c[l]:
                        return 0
                    
                    ans += smap[l]
                    # print(ans)
            
            # print(subset, ans)
            return ans
                
        self.ans = 0
        # Backtrack function to generate all available subsets
        def backtrack(words, subset, index):
            self.ans = max(self.ans, calScore(subset))
            for i in range(index, len(words)):
                subset.append(words[i])
                helper(words, subset, i+1)
                subset.pop(-1)
                
        backtrack(words, [], 0)
        
        return self.ans
