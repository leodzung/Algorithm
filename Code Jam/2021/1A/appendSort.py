# The idea is to be greedy when updating a number
# We will make it smallest possible number that larger than the one before it
N = int(input())

for i in range(1, N+1):
    length = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    for j in range(1, length):
        # If the number is not strictly larger than the one before it
        if arr[j] <= arr[j-1]:
            # Make the two numbers equal length
            k = 0
            while arr[j]*10**k <= arr[j-1]:
                k += 1
            
            # If the curren number is a prefix of the number before it
            if arr[j]*10**(k-1) <= arr[j-1] < arr[j]*10**(k-1)+10**(k-1)-1:
                ans += k-1
                arr[j] = arr[j-1]+1
            # Otherwise, we need to add 0
            else:
                arr[j] = arr[j]*10**k
                ans += k

    print(f'Case #{i}: {ans}')
