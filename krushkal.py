class Graph:    #class to represent a graph
    def __init__(self, vertices):
        self.V = vertices #number of vertices
        self.graph = []  #the brackets are used to store graph

    def add_edge(self, u, v, w):#this will add an edge between the nodes
        self.graph.append([u, v, w])

    # Search function

    def find(self, parent, i):# path to be find
        if parent[i] == i: #if parent node is same as i 
            return i
        return self.find(parent, parent[i])
# function that does union of sets x and y
    def apply_union(self, parent, rank, x, y):#small rank tree under root of high rank tree
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:  #if both the ranks are same then make one as the root
            parent[yroot] = xroot
            rank[xroot] += 1

    #  Applying Kruskal algorithm
    def kruskal_algo(self):
        result = []    #this will sorte the minimum spanning tree
        i, e = 0, 0   #i is used for sorted edges , e is used for result[]
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []   #parent node to be stored
        rank = []      #rank to be stored
        for node in range(self.V):#self.V is declared in 
            parent.append(node)#init
            rank.append(0)#init
        while e < self.V - 1:  #we know that in k  no of e = n-1 nodes
            u, v, w = self.graph[i]#take the smallest edge & satisfy instruct and increment
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            #as we know that in a set the repeatatve nodes are nt consider
            #as they result in the for mation of cycle (which we need to ignore)
            #so inorder to ignore the cycle we see if that node and the
            #parent node are in the not in same set we eill execute this if statement
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
                #else discard the edge
                # this will be stored as in result
        for u, v, weight in result:
            print("%d - %d: %d" % (u, v, weight))


g = Graph(6)#total 6 nodes
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 2)
g.add_edge(1, 0, 4)
g.add_edge(2, 0, 4)
g.add_edge(2, 1, 2)
g.add_edge(2, 3, 3)
g.add_edge(2, 5, 2)
g.add_edge(2, 4, 4)
g.add_edge(3, 2, 3)
g.add_edge(3, 4, 3)
g.add_edge(4, 2, 4)
g.add_edge(4, 3, 3)
g.add_edge(5, 2, 2)
g.add_edge(5, 4, 3)
g.kruskal_algo()#execute member func
