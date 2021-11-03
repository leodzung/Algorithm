def stoneGameII(self, piles: List[int]) -> int:
        N = len(piles)
        
        @lru_cache(None)
        def cal(i, m):
            S = sum(piles[i:])
            if 2*m >= N-i:
                return S
            
            ans = 0
            for x in range(1, 2*m+1):
                ans = max(ans, S-cal(i+x, max(m, x)))
            
            return ans
        
        return cal(0, 1)
