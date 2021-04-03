def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1 = sentence1.split()
        words2 = sentence2.split()
        # print(words1, words2)
        
        def isSimilar(words1, words2):
            left, right = 0, len(words1)-1
            
            while left < len(words2) and words1[left] == words2[left]:
                left += 1
                
            while right > 0 and words1[right] == words2[len(words2)-(len(words1)-right)]:
                right -= 1
                
            print(left, right)
            if right < left or right-left+1 == len(words1)-len(words2):
                return True
            return False
        
        if len(words1) < len(words2):
            return isSimilar(words2, words1)
        
        return isSimilar(words1, words2)
