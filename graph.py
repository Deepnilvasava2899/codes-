def add_vertex(v):  #node allocated function
    global graph
    global vertex_no  #modify the variable outside the current scope
    if v in graph:    #if the element are same
        print("vertex",v,"already exists.")
    else:
        vertex_no=vertex_no +1 #if not then append
        graph[v]=[]

#to add a edge between specific nodes eg btween v1 and v2
def addedge(v1,v2,e):
    global graph
    if v1 not in graph:#checks whether ther is v1 node or not
        print("vertex",v1,"doesnot exists")
    elif v2 not in graph:#checks whether the node v2 si there in the graph
        print("vertex",v2,"doesnot exists")
    else:
        temp=[v2,e]
        graph[v1].append(temp)#graph with node v1 -> will be appended thorugh edge e
        #graph[v2].append(v1)#this ill make an undrireced graph
        #graph[v2].append(v2)#indirected plus un weighted


#now to print the graph

def print_graph():
    global graph
    for vertex in graph:#two loops
        for edges in graph[vertex]:
            print(vertex, " -> ", edges[0], " edge weight: ", edges[1])

graph = {} #dictionary
# stores the number of vertices in the graph
vertex_no = 0
add_vertex(1)
add_vertex(2)
add_vertex(3)
add_vertex(4)
# Add the edges between the vertices by specifying
# the from and to vertex along with the edge weights.
addedge(1, 2, 1)#(v1->v2, their weight)
addedge(1, 3, 1)
addedge(2, 3, 3)
addedge(3, 4, 4)
addedge(4, 1, 5)
print_graph()
# Reminder: the second element of each list inside the dictionary
# denotes the edge weight.
print ("Internal representation: ", graph)
