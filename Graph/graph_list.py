def add_graph(v):
    if v in graph:
        print('node already present in graph')
    else:
        graph[v]=[]

#adding edges with out cost or values
def add_edge(v1,v2):
    if v1 not in graph:
        print(v1,' not present in graph')
    elif v2 not in graph:
        print(v2,'not in graph')
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)

#adding edges with values or cost
def add_edges(v1,v2,cost):
    if v1 not in graph:
        print(v1,' not present in graph')
    elif v2 not in graph:
        print(v2,'not in graph')
    else:
        list1=[v2,cost]
        list2=[v1,cost]
        graph[v1].append(list1)
        graph[v2].append(list2)

#directed graph
def delete_graph(v):
    if v not in graph:
        print(v,'not in graph')
    else:
        graph.pop(v)
        for i in graph:
            list1=graph[i]
            if v in list1:
                list1.remove(v)

#un-directed graph with cost
def delete_graph_cost(v):
    if v not in graph:
        print(v,'not in graph')
    else:
        graph.pop(v)
        for i in graph:
            list1=graph[i]
            for j in list1:
                if v==j[0]:
                    list1.remove(v)
                    break

graph={}
print('before adding',graph)
add_graph('A')
add_graph('B')
add_graph('C')
print('after adding',graph)
add_edges('A','B',5)
add_edges('B','C',10)
add_edges('A','C',2)
print(graph)