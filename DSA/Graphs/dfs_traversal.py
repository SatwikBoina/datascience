

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

    def dfs_traversal(self,start):
        is_visited = {k : False for k in self.vertices}
        dfs_result = []

        def dfs_recursive(start,is_visited,dfs_result):
            print(start)
            start_index = self.get_index(start)
            dfs_result.append(start)
            is_visited[start] = True
            for i in range(len(self.vertices)):
                if  start_index== i:
                    continue
                if self.adj_matrix[start_index][i] == 1 and is_visited[self.vertices[i]]==False:
                    dfs_recursive(self.vertices[i],is_visited,dfs_result) 
            
        dfs_recursive(start,is_visited,dfs_result)

        return dfs_result


nodes = ['A', 'B', 'C', 'D']
edges = [
    ('A', 'B', 1),
    ('A', 'C', 1),
    ('B', 'C', 1),
    ('B', 'D', 1),
    ('C', 'D', 1)
]
nodes = ['X', 'Y', 'Z', 'W']
edges = [
    ('X', 'Y', 1),
    ('Y', 'Z', 1),
    ('Z', 'X', 1),
    ('Z', 'W', 1)
]

graph_demo = Graph()
for node in nodes:
    graph_demo.add_vertex(node)

for source,destination,weight in edges :
    graph_demo.add_edge(source,destination,weight)

graph_demo.display()

print(graph_demo.dfs_traversal("X"))