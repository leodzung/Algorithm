def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head
        
        stack = []
        stack.append(head)
        # We need to create this node for the head when there is no previous node
        prev = Node(0)
        
        while stack:
            node = stack.pop()
            
            # Connect the current node with the previous node
            node.prev = prev
            prev.next = node
            
            # Add the next and the child nodes to stack
            # We add the next node first and the child node later to process the child node first
            if node.next:
                stack.append(node.next)
                node.next = None
            if node.child:
                stack.append(node.child)
                node.child = None
                
            # The current node becomes the previous node
            prev = node
            
        # Since we created the dummy node as the previous node for head, now we have to undo it
        head.prev = None
        return head  
