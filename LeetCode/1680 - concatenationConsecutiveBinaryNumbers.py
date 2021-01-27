 bitshift = ans = 0
        
for i in range(1, n+1):
    # Check if i is the power of 2
    if i & (i-1) == 0:
        # If it is, we need to shift 1 further
        bitshift += 1

    # We shift the ans and then add i
    ans = (ans<<bitshift|i) % (10**9+7)

return ans
