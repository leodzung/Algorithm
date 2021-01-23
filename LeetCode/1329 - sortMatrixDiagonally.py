def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        # The idea is to use a hashmap to store the diagonals
        # Note that in each diagonal, the difference between row index and col index are the same among elements, and unique among diagonals.
        m, n = len(mat), len(mat[0])
        mmap = {}
        
        for i in range(m):
            for j in range(n):
                # Use the difference between row and col indices as the id
                if (i-j) not in mmap:
                    mmap[i-j] = [mat[i][j]]
                else:
                    mmap[i-j].append(mat[i][j])
             
        # Sort the diagonals
        for key in mmap.keys():
            mmap[key].sort(reverse=True)
            
        # Repopulate the matrix
        for i in range(m):
            for j in range(n):
                mat[i][j] = mmap[i-j].pop()
                
        return mat
