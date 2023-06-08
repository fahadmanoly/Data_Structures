def add_node(v):
    global node_count
    if v in node:
        print('already present')
    else:
        node_count=node_count+1
        node.append(v)
        for n in graph:
            n.append(0)
        temp=[]
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)

def add_edge(v1,v2,cost):
    if v1 not in node:
        print(v1,'No such node')
    elif v2 not in node:
        print(v2,'no such node')
    else:
        index1=node.index(v1)
        index2=node.index(v2)
        graph[index1][index2]=cost
        graph[index2][index1]=cost


def display_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(format(graph[i][j], "< 3"),end=' ')
        print()

def delete_graph(v):
    global node_count
    if v not in node:
        print('node not present in the graph')
    else:
        node_count = node_count-1
        index1=node.index(v)
        node.remove(v)
        graph.pop(index1)
        for i in graph:
            i.pop(index1)

def delete_edge(v1,v2):
    if v1 not in node:
        print(v1,'node not present')
    elif v2 not in node:
        print(v2,'node not present')
    else:
        index1=node.index(v1)
        index2=node.index(v2)
        graph[index1][index2]=0
        graph[index2][index1]=0


node=[]
graph=[]
node_count=0
print('node before adding',node)
print('graph before adding',graph)
add_node('A')
add_node('B')
add_node('C')
add_node('D')
add_edge('A','B',10)
add_edge('B','C',5)
add_edge('A','D',15)
add_edge('A','C',20)
add_edge('B','D',25)
add_edge('C','D',30)
print('node after adding',node)
display_graph()
delete_edge('C','B')
print('after deletion of node',node)
display_graph()







