def findTheLongestSubstring(self, s: str) -> int:
        cur = 0
        prefix = [cur]
        for char in s:
            if char == 'a':
                cur ^= 1 << 0
            elif char == 'e':
                cur ^= 1 << 1
            elif char == 'i':
                cur ^= 1 << 2
            elif char == 'o':
                cur ^= 1 << 3
            elif char == 'u':
                cur ^= 1 << 4
            prefix.append(cur)
            
        N = len(s)
        for length in range(N, 0, -1):
            for left in range(N-length+1):
                right = left+length
                if prefix[left] == prefix[right]:
                    return length
        return 0
