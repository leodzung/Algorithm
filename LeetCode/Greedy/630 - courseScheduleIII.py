from heapq import heappush, heappop

class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        # We go through courses and prioritize the deadline
        courses.sort(key=lambda x: x[1])
        # Maintain the list of current courses
        cur = []
        
        # Current date
        date = 0
        for i in range(len(courses)):
            # If we can still add the current course
            if date+courses[i][0] <= courses[i][1]:
                heappush(cur, -courses[i][0])
                date += courses[i][0]
            # Otherwise, in the list of current courses the one with longest duration to swap 
            elif cur and -cur[0]>courses[i][0]:
                date += courses[i][0] + heappop(cur)
                heappush(cur, -courses[i][0])
            # If this swapping doesn't work, we know we don't have any other better option to swap -> move on
                
        return len(cur)
