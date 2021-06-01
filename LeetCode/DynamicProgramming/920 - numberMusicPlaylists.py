from functools import lru_cache

class Solution(object):
    def numMusicPlaylists(self, N, G, K):
        """
        :type n: int
        :type goal: int
        :type k: int
        :rtype: int
        """
        @lru_cache(None)
        def dp(g, n):
            # g = 0, n = 0 -> f = 1
            if g == 0:
                return +(n == 0)
            
            # Build from playlists of g-1 songs, with n-1 different songs, and pick randomly 1 new song from remaining N - (n-1)
            # K doesn't matter because the new song will not violate this constraint
            ans = dp(g-1, n-1) * (N-(n-1))
            
            # Build from playlist of g-1 songs, with n different songs -> new song has already been played.
            # We have to avoid the last K songs -> total songs available = n-K
            ans += dp(g-1, n) * max(n-K, 0)
            
            return ans % (10**9+7)
            
        
        return dp(G, N)
