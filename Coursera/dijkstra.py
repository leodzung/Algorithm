from heapq import heapify, heappush, heappop

class Dijkstra:
    def __init__(self, file='dijkstraData.txt'):
        # Reading file
        file = open(file)
        lines = file.read().split('\n')
        # self.edges = [[int(i) for i in s.split()] for s in self.edge

        self.edges = {}

        for line in lines:
            items = line.split("\t")

            # The tuple (head, length) starting from index 1
            for i in range(1, len(items)):
                if items[i]:
                    vertex, length = items[i].split(',')

                    # The first number of the line is the tail vertex
                    # Convert it into int
                    sourceVertex = int(items[0])

                    # Save the edges and lengths into self.edges
                    if sourceVertex not in self.edges:
                        self.edges[sourceVertex] = [(int(vertex), int(length))]
                    else:
                        self.edges[sourceVertex].append((int(vertex), int(length)))

    # Running Dijkstra from src vertex
    def run(self, src):

        # Initialize the heap with the source vertex with length 0
        minHeap = [(0, src)]

        # Track current shortest path so far from source vertext to current vertext
        mins = {src:0}

        # This is used to track whether we visited the current vertex when considering it
        # Also keep track of the shortest path
        self.seen = {}

        while minHeap:
            # Get the current vertex with the shortest key from the heap
            length, source = heappop(minHeap)
            # print(source, length)

            # If the current vertex hasn't been seen before, market as seen and the shortest path as length
            if source not in self.seen:
                self.seen[source] = length

                # Update the vertex that has source vertex as tail
                if source in self.edges:
                    for destination, l in self.edges[source]:
                        # print(source, destination)

                        # If the destination has alredy been seen before, it has already been process and is skipped
                        if destination in self.seen.keys():
                            continue
                        
                        prev = mins.get(destination, None)
                        next = length + l

                        # Update key if the current value is None (can also be thought of as +inf)
                        # Or the current value is larger than the current shortest path + length(source -> destination)
                        # This is Dijkstra's greedy formula
                        if prev is None or next < prev:
                            mins[destination] = next
                            heappush(minHeap, (next, destination))


        return float('inf')

dijkstra = Dijkstra()
dijkstra.run(1)
# print(dijkstra.edges)
for vertex in [7,37,59,82,99,115,133,165,188,197]:
    print(dijkstra.seen[vertex])
