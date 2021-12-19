def decodeString(self, s: str) -> str:
        ans, count = "", ""
        stack = []
        
        for i, char in enumerate(s):
            if char.isnumeric():
                count += char
            elif char not in '[]':
                if len(stack) == 0:
                    ans += char
                else:
                    stack[-1][1] += char
            elif char == '[':
                stack.append([count, ""])
                count = ""
            else:
                num, string = stack.pop()
                if stack:
                    stack[-1][1] += string * int(num)
                else:
                    ans += string * int(num)
        
        return ans  
