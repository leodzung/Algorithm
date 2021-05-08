from collections import defaultdict
from timeit import default_timer as timer

# The idea is to BFS all the neighbors with less-than-3 distance from a node
class Clustering:
    def _readInput(self, file):
        start = timer()
        print("Start reading input...")
        file = open(file)
        lines = file.read().split('\n')

        NUM_NODES, self.NUM_BITS = map(int, lines[0].split())

        self.nodes = []
        # In the beginning, each node is its own cluster. Starting with 1
        cluster = 1
        # Mapping each node with each cluster
        self.clusters = defaultdict(int)
        for i in range(1, len(lines)-1):
            num = int(''.join(lines[i].replace(" ", "")), 2)
            self.nodes.append(num)
            self.clusters[num] = cluster
            cluster += 1

        end = timer()
        print("End reading input: ", end-start)

    # Create a list of bit masks with 2 1-bits. This will be use to find the neighbors of a node
    def _createHamm(self):
        self.hamm = [0]*300
        k = 0

        for i in range(self.NUM_BITS):
            for j in range(i, self.NUM_BITS):
                mask1, mask2 = 1 << i, 1 << j
                self.hamm[k] = mask1|mask2
                k += 1

    def __init__(self, file='clustering_big.txt'):
        self._readInput(file)
        self._createHamm()

    def _neighbors(self, x):
        for i in self.hamm:
            # We know that x^i is a valid node when it has a non-zero cluster
            if self.clusters[x^i] != 0:
                yield x^i

    def run(self):
        start = timer()
        print("Start clustering...")
        ans = []

        for i, node in enumerate(self.nodes):
            # print("Processing node # ", i, " : ", node)
            # If this node belongs to a processed cluster, skip processing it because we should already have processed it and its neighbors
            if self.clusters[node] in ans:
                continue

            # Start from the current node
            curNodes = [node]
            while curNodes:
                newNodes= []
                for n in curNodes:
                    # Process all the neighbors of the current node. Merge them to the same cluster.
                    for neigh in self._neighbors(n):
                        if self.clusters[n] != self.clusters[neigh]:
                            self.clusters[neigh] = self.clusters[n]
                            newNodes.append(neigh)
                
                # Process the neighbor list
                curNodes = newNodes

            # All the node in this cluster has been processed. Add this to the done list.
            ans.append(self.clusters[node])

        end = timer()
        print("End clustering", end-start)
        print(len(ans))

clustering = Clustering()
clustering.run()
