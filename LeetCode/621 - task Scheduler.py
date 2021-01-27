from collections import Counter

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # The idea is that the most frequent char is also most important
        # Regardless of n and available chars, the sequence will always end with the most frequent char
        # If n < available chars, task sequence will be in format: T1, T2, ... Tn, T1, T2, ..., Tn
        # If n > available chars, task sequence will be in format: T1, T2, ... idle, T1, T2, ..., Idle
        # Where T1, T2, T3 are sorted by their frequency
        
        # We sort the task by frequency
        char_freq = sorted(Counter(tasks).values(), reverse = True)
        # print(char_freq)
        
        index, counter, max_freq = 0, 0, char_freq[0]
        
        # We only care about the characters that has the (same) max frequency
        while index < len(char_freq) and char_freq[index] == max_freq:
            # print(index)
            counter += 1
            
            # Each chunk is of the length (n+1)
            # There are max_freq numbers of those chunks
            # Notice that in the end, there are multiple char with the same max_frequency will be left over
            # Example 1: tasks = ["A","A","A","B","B","B"], n = 2
            # A -> B -> idle -> A -> B -> idle -> A -> B: there are 2 chunks of length (2+1)
            # A and B is left over, so we have to account for that with the counter (=2 in this case)
            result = (max_freq - 1) * (n + 1) + counter
            # print(result, max_freq, n, counter)
            
            index += 1
            
        # If n too small, we actually can have a case that result < len(tasks)
        # Example 2: tasks = ["A","A","A","B","B","B"], n = 0
        # In such cases, we should return len(tasks)
        return max(result , len(tasks))
