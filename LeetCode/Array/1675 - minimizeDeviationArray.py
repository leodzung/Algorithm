def minimumDeviation(self, nums: List[int]) -> int:
        """
        Observation: we can only increase the odd number, and we can only decrease the even number
        Therefore, if we increase all the odd numbers, we only have to consider whether to decrease a number
        Afterward, we can try to decrease the current max to reduce deviation (since now we cannot increase the min)
        """
        
        # Heap to support the extract max operation
        # Note that we have to flip sign of the number in evens because Python only support min heap
        evens = []
        
        # Current minimum number in heap. Use this to calculate current deviation
        minimum = 0
        
        # Double all the odd number, and flip sign of all numbers
        for num in nums:
            if num%2 == 0:
                evens.append(-num)
            else:
                evens.append(-num*2)
        
        # Get the current minimum
        minimum = -max(evens)
        # print(minimum, evens)
        
        heapq.heapify(evens)
        
        ans = inf
        
        while evens:
            # Extract max. Note that we have to flip the sign to get the original number
            current_value = -heapq.heappop(evens)
            # print(current_value, evens)
            
            # Calculate current deviation
            ans = min(ans, current_value - minimum)
            # print(ans)
            
            # If the current max is even, we can half it and push it back to the heap
            if current_value % 2 == 0:
                minimum = min(minimum, current_value//2)
                heapq.heappush(evens, -current_value//2)
            
            # Else the current max is the actual max (because it cannot be reduced any further)
            # In such cases, stop operation
            else:
                break
                
        return ans
