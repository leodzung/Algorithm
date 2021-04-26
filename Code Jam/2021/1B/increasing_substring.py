T = int(input())

for i in range(1, T+1):
    N = int(input())
    s = str(input())
    
    dp = [1] * N
    
    for j in range(1, N):
        if s[j] > s[j-1]:
            dp[j] = dp[j-1]+1
    
    ans = ' '.join([str(num) for num in dp])
    print(f'Case #{i}: {ans}')
