class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        
        def backTrack(strList: list, curStr:str, strSet:set):
            # If there is no more char to take from the list, return
            print(strList)
            if not strList:
                return 
            
            # Append each char in list to current string
            for char in strList:
                newStr = curStr + char
                # Add curStr to the answer set if not there already
                if newStr not in strSet:
                    strSet.add(newStr)
                    
                # Copy a new list to back track
                newList = strList.copy()
                
                # Remove the last added char
                newList.remove(char)
                
                backTrack(newList, newStr, strSet)
                
        ans = set()
        backTrack(list(tiles), "", ans)
        
        # print(ans)
        return len(ans)
