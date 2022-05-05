class MyCalendarTwo(object):

    def __init__(self):
        self.events = []
        self.overlaps = []
        
    def getOverlap(self, start1, end1, start2, end2):
        return max(start1, start2) , min(end1, end2)
        
    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        overlaps = []
        for s, e in self.events:
            startOverlap, endOverlap = self.getOverlap(start, end, s, e)
            if endOverlap > startOverlap:
                overlaps.append((startOverlap, endOverlap))
                
        for overlap in overlaps:
            for currentOverlap in self.overlaps:
                startOverlap, endOverlap = self.getOverlap(overlap[0], overlap[1], currentOverlap[0], currentOverlap[1])
                if endOverlap > startOverlap:
                    return False
                
        self.overlaps += overlaps
        self.events.append((start, end))
        return True
