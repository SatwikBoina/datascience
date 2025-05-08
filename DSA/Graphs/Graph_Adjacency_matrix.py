# adjacency matrix : Maintain a matrix (nxn) to represent the connection between the nodes.
# Not advisable to use this for a Sparse graph(less number of edges), As this way occupies space. A lot of space goes waste with the lack of unrepresenation.

class Graph :
    def __init__(self,vertices_list:list = []):
        self.vertices = vertices_list
        self.num_of_nodes = len(vertices_list)
        self.adj_matrix  = [None]*len(self.vertices)

    def get_index(self,vertex):
        return self.vertices.index(vertex)

    def add_vertex(self,vertex):
        if vertex not in self.vertices:
            self.vertices.append(vertex)
            self.num_of_nodes+=1
        
    def initialize_adj_matrix(self):
        self.adj_matrix = [[0]*self.num_of_nodes for row in range(self.num_of_nodes)]
            
        
    def add_edge(self,source,destination,weight =1):

        if self.num_of_nodes != len(self.adj_matrix):
            self.initialize_adj_matrix()
        
        if 0<= self.get_index(source) < self.num_of_nodes and 0<= self.get_index(destination) < self.num_of_nodes:
            self.adj_matrix[self.get_index(source)][self.get_index(destination)] = weight

        

        
    def display(self):

        for index,connections in enumerate(self.adj_matrix):
            print(f"{self.vertices[index]}:{connections}")


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