# Graph Creation using Edge List

# What are the max number of edges a graph of "n" nodes can have?
class Graph :
    def __init__(self):
        self.vertices = []
        self.edges = []
    def __repr__(self):
        graph = { k : [] for k in self.vertices}
        for source,destination,weight in self.edges :
            graph[source].append((source,destination,weight))
        return f"Graph : {graph}"


    def add_vertex(self,vertex):
        if vertex not in self.vertices:
            self.vertices.append(vertex)
    
    def add_edge(self,source,destination,weight =1):
        if (source,destination,weight) not in self.edges:
            self.edges.append((source,destination,weight))


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

print(graph_demo)