def nextGreaterElement(self, n: int) -> int:
        # Space: O(N)
        s = list(str(n))
        
        mxDigit = None
        # Time: O(N)
        for i in range(len(s)-1, 0, -1):
            if not mxDigit or mxDigit < s[i]:
                mxDigit = s[i]
                
            if mxDigit > s[i-1]:
                s[i:] = sorted(s[i:])
                j = i
                while s[i-1] >= s[j]:
                    j += 1
                s[i-1], s[j] = s[j], s[i-1]
                nxt = int(''.join(s))
                return nxt if nxt <= 2**31-1 else -1
            
        return -1
