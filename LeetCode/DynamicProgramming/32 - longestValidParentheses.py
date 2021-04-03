def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        
        dp = [0 for _ in range(len(s))]
        
        ans = 0
        for i, char in enumerate(s):
            # We only need to update dp when char = ')'
            if i > 0 and char == ')':
                # If the substring has the form of "substring1()"
                if s[i-1] == '(':
                    dp[i] = dp[i-2]+2
                # If the substring has the form of "substring1))", consider the longest substring ends at i-1
                # If before that substring is char '(' then we can combine it with the current ')'
                elif i-dp[i-1] and s[i-dp[i-1]-1] == '(':
                    dp[i] = dp[i-1]+2
                    # There can be a longest substring preceding the newly formed substring
                    # Format: "substring1(substring2)", in which "(substring2)" is the newly form substring
                    # We can then combine them to make an even longer substring
                    if i-dp[i-1]>=2:
                        dp[i] += dp[i-dp[i-1]-2]
                
                ans = max(ans, dp[i])
        return ans
