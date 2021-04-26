def movesToStamp(self, stamp, target):
        """
        :type stamp: str
        :type target: str
        :rtype: List[int]
        """
        M, N = len(stamp), len(target)
        
        # To keep all the done indices and propagate
        queue = deque()
        # We only add to queue the index that hasn't been done yet
        done = [False] * N
        
        # Keep track of whether the current window is made or not
        A = []
        
        ans = []
        
        # Process all windows starting from i
        for i in range(N-M+1):
            # Set of indices that match the stamp and one of those that don't
            made, todo = set(), set()
            
            for j, char in enumerate(stamp):
                if target[i+j] == char:
                    made.add(i+j)
                else:
                    todo.add(i+j)
            A.append((made, todo))
            
            # If TODO list is empty, then the current window is made.
            if not todo:
                ans.append(i)
                for j in range(i, i+len(stamp)):
                    if not done[j]:
                        queue.append(j)
                        # Mark all index in the windows as done
                        done[j] = True
          
        # Process all index in queue, which are already done
        while queue:
            i = queue.popleft()
            
            # Go through all the windows that has the current index
            for start in range(max(0, i-M+1), min(N-M, i)+1):
                # If current index is in the todo list of the current window, we remove it
                if i in A[start][1]:
                    A[start][1].discard(i)
                    # If after removing the current index the window is done
                    if not A[start][1]:
                        ans.append(start)
                        # We mark all the other index in the window as done and as them to queue
                        for m in A[start][0]:
                            if not done[m]:
                                queue.append(m)
                                done[m] = True
                            
        # If al the indices are done, we have the answer
        return ans[::-1] if all(done) else []
