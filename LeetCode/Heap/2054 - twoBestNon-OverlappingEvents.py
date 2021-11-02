def maxTwoEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        # Sort events by start time
        events.sort()
        ans = 0
        
        # We maintain this heap of only the events that might overlap
        # Means that the ends of these events were larger that the start of the last one pushed into the heap
        # Also means that the ones got popped won't overlap with any subsequent events
        seen_events = []
        
        # This is to keep track of the event with the maximum value among the events popped
        mevent = 0
        
        for start, end, val in events:
            # Process the events in the heap that do not overlap with the current event
            while seen_events and seen_events[0][0] < start:
                e, v = heappop(seen_events)
                # Update the maximum value of the popped events
                mevent = max(mevent, v)
            
            ans = max(ans, val+mevent)
            heappush(seen_events, (end, val))
        return ans
