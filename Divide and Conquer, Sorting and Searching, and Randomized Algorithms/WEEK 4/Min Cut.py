import random
def graphify(lines):
    g = dict()
    for line in lines:
        data = (line.strip().split("\t"))
        vLabel = data[0]
        g[vLabel] = []
        for vertex in data[1:]:
            g[vLabel].append(vertex)
    return g

def mincut(g):
    while len(g) > 2:
        vertex1 = random.choice(list(g.keys()))
        vertex2 = random.choice(g[vertex1]) # chose a vertex adjacent to vertex1
        contract(g,vertex1,vertex2) # merge two vertices
    return len(g[list(g.keys())[0]]) # length of current cut is given by neighbor of one of the super nodes

def contract(g,v,w):
    for node in g[w]: # for every node adjacent to w
        if node != v: # if the node is not the same with v, other vertex to contract with
            g[v].append(node) # append the node as a neighbor 
        g[node].remove(w) # remove the edge from node to w since w will be lost
        if node != v:
            g[node].append(v) # append v(super node) as a neighbor
    del g[w]

with open("kargerMinCut.txt","r") as f:
    lines = f.readlines()
    g = graphify(lines)

vertexCount = len(g)
minVal = vertexCount * (vertexCount-1) / 2
for i in range(300):
    currCut = mincut(g)
    if currCut <= minVal:
        minVal = currCut
    g = graphify(lines)
#print(minVal)
