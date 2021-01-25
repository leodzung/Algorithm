class Solution(object):
    """
    The idea is to merge a pair of linked lists at a time
    Then recursively call the function on the merged lists
    The number of lists will be reduced by half after each iteration
    """
    
    def merge2Lists(self, list1, list2):
        """
        Helper function to merge two list
        """
        
        # If one of the list is empty, return the other
        if not (list1 and list2): return list1 or list2
    
        # Create an dummy node to return
        current = ans = ListNode()
        
        while list1 and list2:
            # Compare value from list1 and list2 to decide which node to take
            if list1.val > list2.val:
                current.next = list2
                list2 = list2.next
            else:
                current.next = list1
                list1 = list1.next
                
            # Move on to the next node
            current = current.next
            
            # If one of the list becomes empty, the assign the next node to the other list
            if not list2:
                current.next = list1
            
            if not list1:
                current.next = list2
            
        return ans.next
                
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        n = len(lists)
        
        # Handle edge case when the lists is empty
        if n == 0:
            return None
        # Base case when there is only one list, return the only list
        if n == 1:
            return lists[0]
        
        # Create the new list to store the merged list of each pair
        newList = []
        for i in range(0, n-1, 2):
            mergeList = self.merge2Lists(lists[i], lists[i+1])
            newList.append(mergeList)
            
        # If we have an odd number of list, append the last list to the new list for the next iteration
        if n%2 == 1:
            newList.append(lists[n-1])
            
        # Call recursive function on the new list
        return self.mergeKLists(newList) 
