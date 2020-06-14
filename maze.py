from collections import defaultdict
import argparse

# creating undirected-unweighted graph


class Graph:
    # Constructor
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)
        self.edges = {}
        self.prev_vertex = {}

    # function to add an edge to graph
    def add_edge(self, u, v):

        self.graph[u].append(v)
        self.graph[v].append(u)

        self.edges[(u, v)] = 1
        self.edges[(v, u)] = 1

    # checking if the path exists between source node and destination node,
    #  if the path exists it will return true,
    # if not then returns false
    # BFS(breadth-first-search) is used to if the path exists or not

    def if_path_exist(self, u, v):

        # Mark all the vertices as not visited
        vertex_visited = {}
        for i in self.graph:
            vertex_visited[i] = False

        # Create a queue for BFS
        queue = []

        # Mark the source node as
        # visited and enqueue it
        queue.append(u)
        vertex_visited[u] = True

        connected_vertices = set()

        while queue:

            # Dequeue a vertex from
            # queue and add the vertex in connected_vertices
            temp = queue.pop(0)
            connected_vertices.add(temp)

            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it

            for i in self.graph[temp]:
                if (vertex_visited[i] is False):
                    vertex_visited[i] = True
                    queue.append(i)

        # if source and destination both present in the connected vertices then
        # path exits and returns true else return false

        if u in connected_vertices and v in connected_vertices:
            return True
        return False

    # Funtion that implements Dijkstra's single source
    # shortest path algorithm for a graph represented
    # using adjacency matrix representation

    def shortestpath(self, node):

        dist = {}
        vertex_visited = {}
        for i in self.graph:

            if i == node:
                dist[(node, i)] = 0
            else:
                dist[(node, i)] = 10**9

        for i in self.graph:
            vertex_visited[i] = False

        temp = node

        # Update dist value of the adjacent vertices
        # of the picked vertex only if the current
        # distance is greater than new distance and
        # and vertex_visited is false

        while vertex_visited[temp] is False:
            vertex_visited[temp] = True
            for i in self.graph[temp]:
                if (vertex_visited[i] is False and dist[(node, i)] >
                        self.edges[(temp, i)] + dist[(node, temp)]):
                    dist[(node, i)] = self.edges[(temp, i)] + \
                        dist[(node, temp)]
                    self.prev_vertex[i] = temp

            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.

            largest = 10**9
            for i in self.graph:
                if vertex_visited[i] is False and dist[(node, i)] < largest:
                    largest = dist[(node, i)]
                    temp = i

        return self.prev_vertex

    # method to give set of source to destination

    def source_to_destination(self, u, v):

        # chechks if path exists
        if self.if_path_exist(u, v) is True:

            # find the shortest path set using dijkastra
            prev_vertex = self.shortestpath(u)

            prev_vertex = list(prev_vertex.items())
            size = len(prev_vertex)
            final_ouput = []
            temp = v
            while temp:
                final_ouput.insert(0, temp)

                if temp == u:
                    break
                for i in range(size):

                    if prev_vertex[i][0] == temp:
                        temp = prev_vertex[i][1]

            final_ouput = set(final_ouput)

            return final_ouput
        else:
            return -1


# ----------------------------------------------DRIVER CODE-------------------
g = Graph()

# file handling

pars = argparse.ArgumentParser()
pars.add_argument('--i', "--inputfile", help='Input File',
                  type=str, default="input.txt")
pars.add_argument('--o', "--outputfile", help='Output File',
                  type=str, default="output.txt")
pars.add_argument('--s', '--sourece', help='add destination', type=str)
pars.add_argument('--d', '--destination', help='add source', type=str)
arg = pars.parse_args()


file = open(arg.i, 'r')
file1 = open(arg.o, 'w')
maze = []

# getting input from input.txt

for data in file:
    [x.strip('\n') for x in data]
    maze.append([int(x) for x in data.split()])

file = open(arg.i, 'r')
file1 = open(arg.o, 'w')

order = len(maze)

# addding edges to the connected nodes/vertex
for i in range(len(maze)):
    for j in range(len(maze[0])):
        if j-1 >= 0 and maze[i][j-1] == 1 and maze[i][j] == 1:
            g.add_edge((i, j-1), (i, j))
        if i-1 >= 0 and maze[i-1][j] == 1 and maze[i][j] == 1:
            g.add_edge((i-1, j), (i, j))
a = arg.s
b = arg.d


if a is None:
    a = (0, 0)
else:
    a = tuple(map(int, a.split(',')))


if b is None:
    b = (len(maze)-1, len(maze[0])-1)
else:
    b = tuple(map(int, b.split(',')))


temp_list = g.source_to_destination(a, b)

output_list = [[0 for i in range(len(maze[0]))]
               for j in range(len(maze))]

# represntig the set output that fromin matrix form

if temp_list == -1:
    output = -1
    file1.write(str(output))
else:
    if type(temp_list) is set:
        for i in range(len(maze)):
            for j in range(len(maze[0])):

                if (i, j) in temp_list:
                    output_list[i][j] = int(1)
                else:
                    output_list[i][j] = int(0)

        for i in output_list:
            for j in i:
                file1.write(f' {str(j)}')
            file1.write('\n')
