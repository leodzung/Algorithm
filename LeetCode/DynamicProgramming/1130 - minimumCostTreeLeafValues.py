def mctFromLeafValues(self, arr: List[int]) -> int:
        # Length of the array
        n = len(arr)
        
        dp = [[0] * (n+1) for _ in range(n+1)] 
        
        for length in range(1, n+1):
            for left in range(n-length+1):
                right = left + length
                
                # If length = 1, this is a leaf and we don't add its value to dp
                if length == 1:
                    dp[left][right] = 0
                else:
                    ans = float('inf')
                    # For each of the index between left and right, build the left tree and right tree
                    for i in range(left+1, right):
                        # Posible value of the current node will be: 
                        # Left tree val + right tree val + max left array * right max array
                        val = dp[left][i] + dp[i][right] + max(arr[left:i]) * max(arr[i:right])
                        
                        # Keep only the minimum possible val of the current node
                        ans = min(ans, val)
                        
                    dp[left][right] = ans
                    
        return dp[0][n]
