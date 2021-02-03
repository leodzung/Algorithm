from collections import Counter

class FreqStack(object):
    """
    The challenge of this problem is that we need to manage 2 parameters at the same time:
    1. Frequency and 2. Order of the items
    The idea is to use a 2D array as a stack of stack. This way we can maintain the order of the items
    Items with different frequency will be managed in different stacks
    """

    def __init__(self):
        self.stack =[[]]

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        # Whenever we push, we have to check if the item already exists starting from the lowest frequency stack
        found = False
        for s in self.stack:
            # If we found a stack that this item is not currently in, add it to the stack
            if x not in s:
                # Update the flag
                found = True
                s.append(x)
                
                # Stop the search to prevent update higher frequency stack
                break
        
        # We didn't find this item in any stack
        # It means that this item exists in all stacks and this will be the new highest frequency
        # Therefore, we will add a new stack, with this item as the first element
        if not found:
            self.stack.append([x])

    def pop(self):
        """
        :rtype: int
        """
        # The answer will be the last item of the last stack
        ans = self.stack[-1].pop()
        
        # After poping the item from the last stack, if the stack becomes empty, we pop it also
        if not self.stack[-1]:
            self.stack.pop()
            
        return ans
