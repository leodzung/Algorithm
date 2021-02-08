"""
    Notice that if a board state is a solution, there is a one-to-one mapping betweeen our queen and its row\
    because a row cannot contain two queens
    Therefore, the idea is for each row we will figure out all possible position to put a queen
    Then try each of the possible position and then backtrack
    """
    def totalNQueens(self, n: int) -> int:
        self.placed = [0 for _ in range(n)]
        # print(self.placed)
        
        self.ans = 0
        """
        Backtracking function to find the next state of the board
        queens: keep track of all the queens' positions in the current board state
        row_index: the next row that we need to put our queen in
        """
        def backtrack(queens, row_index):
            # If we found all n queens
            if row_index == n:
                # print(states)
                # Solution found
                self.ans += 1
                
            # Keep track of all possible placement for the next queen
            possible_places = []
            
            # For each of the column index
            for col in range(n):
                # Try to see if the current position would make the new queen collide with existing queens
                collide = False
                for r, c in queens:
                    # There is already a queen occupying this row
                    if col == c:
                        collide = True
                        break
                        
                    # There is already a queen occupying the topleft-bottomright diagonal
                    if col - row_index == c - r:
                        collide = True
                        break
                        
                    # There is already a queen occupying the topright-bottomleft diagonal
                    if col - c == r - row_index:
                        # print(col, row_index, r, c)
                        collide = True
                        break
                        
                # If there is no collision, this is a valid board state
                if not collide:
                    possible_places.append((row_index, col))
                    
            # For each of the valid board state, recurse to explore the placement for the next queen
            for place in possible_places:
                queens.append(place)
                backtrack(queens, row_index+1)
                
                # Pop to backtrack
                queens.pop()
                    
        # Explore from the empty board state
        backtrack([], 0)
        
        return self.ans
