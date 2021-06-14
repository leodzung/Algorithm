def movesToChessboard(self, board):
        N = len(board)
        
        ans = 0
        for count in (
                    # Count lines for row
                    collections.Counter(map(tuple, board)),
                    # Count lines for column
                    collections.Counter(zip(*board))):
            
            # The number of unique lines should be 2
            # The counts should both be N/2 if N is even, and N/2 and (N+1)/2 if N is odd
            if len(count) != 2 or sorted(count.values()) != [N/2, (N+1)/2]:
                return -1
            
            line1, line2 = count
            # Two lines has to be exact opposite
            if not all(x^y for x, y in zip(line1, line2)):
                return -1
            
            # Create a target lines starting with 0 and 1 accordingly if N is even
            # Or starting with whichever value having more frequency if N is odd
            starts = [+(line1.count(1) * 2 > N)] if N%2 else [0,1]
            
            # The number of swaps is a half of the number of differences
            ans += min(sum((i-x)%2 for i, x in enumerate(line1, start)) for start in starts) / 2
            
        return ans
