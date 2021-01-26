def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # If length of the list is less than 2, we don't need to rearrange
        if not head or not head.next:
            return head
        
        # This variable is to keep track which turn is this
        isOdd = True
        
        # Keep track of the odd list
        oddHead = currentOdd = head
        
        # Keep track of the even list
        evenHead = currentEven = head.next
        
        # Start with the third node
        current = head.next.next
        while current:
            if isOdd:
                # print(current.val)
                currentOdd.next = current
                currentOdd = currentOdd.next
            else:
                # print(current.val)
                currentEven.next = current
                currentEven = currentEven.next
                
            # Swap turn    
            isOdd = not isOdd
            current = current.next
                
        # We need to end the even list, otherwise we will get cycled list                
        currentEven.next = None
        
        # Point the odd list to the even list
        currentOdd.next = evenHead
        
        # The odd list is the result
        return oddHead    
