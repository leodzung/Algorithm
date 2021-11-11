def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        counter = defaultdict(int)
        
        for row in matrix:
            z, o = 0, 0
            for i, num in enumerate(row):
                # 110
                if num:
                    o |= 1 << i
                # 
                # Shift left i times
                # 1, after shifting 3 times: 1000b = 8 (dec)
                else:
                    z |= 1 << i
            counter[o] += 1
            counter[z] += 1
        
        # print(counter)
        
        return max(counter.values())
