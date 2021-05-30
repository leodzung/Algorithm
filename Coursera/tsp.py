from itertools import combinations

class TSP:
    def __init__(self, file='tsp.txt') -> None:
        lines = open(file).readlines()

        self.NUM_CITY = int(lines[0])
        
        cities = []
        for i in range(1, len(lines)):
            x, y = map(float, lines[i].split())
            cities.append((x, y))

        # Pre-calculate the distance among cities before run
        self.dist = [[0]*self.NUM_CITY for _ in range(self.NUM_CITY)]
        for i in range(self.NUM_CITY):
            for j in range(self.NUM_CITY):
                if i != j:
                    self.dist[i][j] = self.distance(cities[i], cities[j])

    def distance(self, city1, city2):
        return ((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2) ** (1/2)

    def run(self):
        dp = [[float('inf')] * self.NUM_CITY for _ in range(1 << self.NUM_CITY)]
        # 1 << 0 = 1
        dp[1][0] = 0

        # Calculate minimum distance from city 0 to other cities
        # Number of subsets = 1 << NUM_CITY
        for i in range(1, 1 << self.NUM_CITY):
            for j in range(self.NUM_CITY):
                for k in range(1, self.NUM_CITY):
                    if j == k:
                        continue
                    # Skip if k is in the subset
                    if (i & (1 << k)) != 0:
                        continue
                    
                    # New subset that includes k
                    p = i | (1 << k)
                    dp[p][k] = min(dp[p][k], dp[i][j] + self.dist[j][k])

        # Add distance from other cities back to city 0 for final answer
        ans = float('inf')
        for j in range(1, self.NUM_CITY):
            ans = min(ans, dp[-1][j] + self.dist[j][0])
        print(ans)

tsp = TSP()
tsp.run()
