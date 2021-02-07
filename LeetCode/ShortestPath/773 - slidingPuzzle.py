def slidingPuzzle(self, board: List[List[int]]) -> int:
        """
        The idea is to use BFS to explore the next states of the current board
        """
        # Board dimensions
        r, c = len(board), len(board[0])
        
        final_state = [[1,2,3],[4,5,0]]
        
        # Keep track of visited states
        visited = set()
        
        # Find the starting index of 0
        br = bc = 0
        for i in range(r):
            for j in range(c):
                if board[i][j] == 0:
                    br, bc = i, j
            
        # Stringify the board to use with hashset
        def stringify(board):
            ans = ""
            
            for i in range(r):
                for j in range(c):
                    ans += str(board[i][j])
                    
            return ans
            
        bq = deque()
        
        # Each item will be the board, row and col index of 0, and the number of step to reach the current state
        bq.append((board, br, bc, 0))
        
        # Mark the orginal board as visited
        og_board = stringify(board)
        # print(og_board)
        visited.add(og_board)
        
        # All possible moves
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while bq:
            board, row, col, num = bq.popleft()
            
            # Final state is reached
            if board == final_state:
                return num
            
            for (dr, dc) in moves:
                # If this move is valid
                if 0 <= row+dr < r and 0 <= col+dc < c:
                    # Create a new board to add to queue
                    new_board = copy.deepcopy(board)
                    new_board[row+dr][col+dc], new_board[row][col] = new_board[row][col], new_board[row+dr][col+dc]
                    
                    str_board = stringify(new_board)
                    # If we haven't seen this board, add it to queue, then mark it as visited
                    if str_board not in visited:
                        bq.append((new_board, row+dr, col+dc, num+1))
                        visited.add(str_board)
        
        return -1
