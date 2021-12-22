def reorderList(self, head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    # Find the middle, so that slow.next will be start of the 2nd half
    fast, slow = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse the 2nd half
    prev, cur = None, slow.next
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    # End the 2nd half
    slow.next = None

    # Merge the two halves
    h1, h2 = head, prev
    while h2:
        nxt = h1.next
        h1.next = h2
        h1 = h2
        h2 = nxt
