class Solution:
    @functools.lru_cache(None)
    def rearrangeSticks(self, n: int, k: int) -> int:
        # Base cases
        if n == k: return 1
        if k == 0: return 0
        
        # Put the tallest (always visible) as the right most position. Need to make k-1 sticks visible from n-1.
        # Or put any of (n-1) other sticks as the right most, which will not be visible as the tallest is in front of it.
        # So still need to arrange to make k sticks visible from n sticks
        return (self.rearrangeSticks(n-1, k-1) + (n-1)*self.rearrangeSticks(n-1, k)) % 1_000_000_007
