def braceExpansionII(self, expression: str) -> List[str]:
        groups = [[]]
        # Control the current level of nested braces
        level = 0
        
        for i, char in enumerate(expression):
            if char == '{':
                # Mark the start of the string inside of the braces to recurse
                if level == 0:
                    start = i+1
                level += 1
            elif char == '}':
                level -= 1
                # Level matches for opening and closing braces -> recurse
                if level == 0:
                    groups[-1].append(self.braceExpansionII(expression[start:i]))
            # Process only when level=0. Other cases will be handled in recursion.
            elif level == 0:
                if char == ',':
                    groups.append([])
                else:
                    groups[-1].append(char)
                    
        ans = set()
        for group in groups:
            ans |= set(map(''.join, itertools.product(*group)))
            
        return sorted(ans)
