# adjacency list : Checking the neighbours of a node. Store which nodes a particular node is closer to

class Graph :
    def __init__(self):
        self.vertices = []
        self.adj_list  = {}

    def add_vertex(self,vertex):
        if vertex not in self.vertices:
            self.vertices.append(vertex)
            self.adj_list[vertex] = []
        
    def add_edge(self,source,destination,weight =1):
        if source in self.vertices and destination in self.vertices:
            self.adj_list[source].append((destination,weight))
            #undirected 
            self.adj_list[destination].append((source,weight))
        else:
            print("Atleast one of the vertices is not found.")
    
    def display(self):

        for vertex,connections in self.adj_list.items():
            print(f"{vertex}:{connections}")


nodes = ['A', 'B', 'C', 'D']
edges = [
    ('A', 'B', 5),
    ('A', 'C', 1),
    ('B', 'C', 4),
    ('B', 'D', 7),
    ('C', 'D', 3)
]
graph_demo = Graph()
for node in nodes:
    graph_demo.add_vertex(node)

for source,destination,weight in edges :
    graph_demo.add_edge(source,destination,weight)

graph_demo.display()