class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # To count the numbers of invalid opening and closing parenthesis
        cleft = cright = 0
        for char in s:
            if char == '(':
                cleft += 1
            elif char == ')':
                if cleft:
                    cleft -= 1
                else:
                    cright += 1
                    
        # print(cleft, cright)
        
        # To store the unique answers
        ans = set()
        def backtrack(pos, cleft, cright, rleft, rright, cur):
            """
            pos: current position in string s
            cleft: the current count of left parenthesis in the current string
            cright: the current count of right parenthesis in the current string
            rleft: the remaining count of the left parenthesis that we will remove
            rright: the remaining count of the right parenthesis that we will remove
            cur: the current string that we are building
            """
            
            # If reached the end of the string
            if pos == len(s):
                # If we removed all the invalid parenthesis, this is a correct answer
                if rleft == rright == 0:
                    # print(cur)
                    ans.add(''.join(cur))
            else:
                # When we still can remove the parenthesis
                if (s[pos] == '(' and rleft) or (s[pos] == ')' and rright):
                    backtrack(pos+1,
                              cleft,
                              cright,
                              rleft-(s[pos]=='('), 
                              rright-(s[pos]==')'),
                              cur
                            )
                    
                # The normal case: keep adding the current character regardless of what it is
                cur.append(s[pos])
                
                # If this is not a parenthesis, just move forward one step
                if s[pos] != '(' and s[pos] != ')':
                    backtrack(pos+1,
                              cleft,
                              cright,
                              rleft, 
                              rright,
                              cur
                            )
                    
                # If this is an opening parenthesis, move forward one step and also increase current left count
                elif s[pos] == '(':
                    backtrack(pos+1,
                             cleft+1,
                             cright,
                             rleft,
                             rright,
                             cur)
                    
                # If this is a closing parenthesis, we only add it if we have more left parenthesis than the right parenthesis
                # This is to ensure that the final answer always valid, i.e. no closing after opening
                elif s[pos] == ')' and cleft > cright:
                    backtrack(pos+1,
                             cleft,
                             cright+1,
                             rleft,
                             rright,
                             cur)
                
                # Pop the current char for backtracking
                cur.pop()
                
        backtrack(0, 0, 0, cleft, cright, [])
        
        
        return list(ans)
