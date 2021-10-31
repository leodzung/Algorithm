def platesBetweenCandles(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # Indexes of the candles
        candles = [i for i, c in enumerate(s) if c=='|']
        print(candles)
        ans = []
        for start, end in queries:
            # The nearest candle on the right of the start
            right_start = bisect.bisect_left(candles, start)
            # The nearest candle on the left of the end
            left_end = bisect.bisect(candles, end) - 1
            
            # The numbers of slots in between a and b = candles[a]-candles[b]-1
            # The numbers of candles in betwwen a and b = a-b-1
            # Therefore the number of plates in between a and b = candle[a]-candes[b] - (a-b)
            ans.append((candles[left_end]-candles[right_start]) - (left_end-right_start) if right_start<left_end else 0)
        
        return ans
