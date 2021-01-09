def maximumGain(self, s: str, x: int, y: int) -> int:
        a, b = 'a', 'b'
        
        # Swap chars and gains if needed
        if x > y:
            a, b = 'b', 'a'
            x, y = y, x
            
        counter = Counter()
        
        ans = 0
        
        # Add a redundant character to handle end-of-string case
        for char in (s + 'x'):
            # print(i, counter[a], counter[b], ans)
            if char in 'ab':
                # If find a, see if we have already seen b
                if char == a:
                    if counter[b] > 0:
                        ans += y
                        counter[b] -= 1
                    else:
                        counter[a] += 1
                # If find b, be greedy and hold off because we might see a later
                else:
                    counter[b] += 1
            else:
                # If see other character, we cannot be greedy anymore and have to combine those as and bs
                ans += min(counter[a], counter[b]) * x
                
                # Reset counter
                counter = Counter()
                
        return ans
