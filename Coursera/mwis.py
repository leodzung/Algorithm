class MWIS:
    def __init__(self, file='mwis.txt'):
        input = list(map(int, open(file).readlines()))
        self.NUM_VERTICES = input[0]
        self.vertices = input[1:]

    def run(self):
        dp = [0] * self.NUM_VERTICES
        dp[0], dp[1] = self.vertices[0], self.vertices[1]

        for i in range(1, self.NUM_VERTICES):
            dp[i] = max(dp[i-1], dp[i-2]+self.vertices[i])
        
        # Reconstruct the indices of the vertices
        s = []
        # Go from right to left
        i = len(dp)-1
        while i >= 0:
            # When the previous case wins, we don't include the current vertices
            if dp[i-1] >= dp[i-2] + self.vertices[i]:
                i -= 1
            else:
                s.append(i)
                i -= 2

        # Construct the answer
        ans = ''
        for i in (1, 2, 3, 4, 17, 117, 517, 997):
            if i-1 in s:
                ans += '1'
            else:
                ans += '0'

        print(ans)

mwis = MWIS()
mwis.run()
