import sys

def makeGraph(graph, M, N):
    for i in range(N):
        graph[i] = [i]
    for _ in range(M):
        [firstNode, secondNode] = list(map(int, sys.stdin.readline().split(" ")))
        
        if firstNode in graph and secondNode not in graph:
            graph[firstNode].append(secondNode)
            graph[secondNode] = [firstNode]
        elif firstNode not in graph and secondNode in graph:
            graph[secondNode].append(firstNode)
            graph[firstNode] = [secondNode]
        else:
            graph[secondNode].append(firstNode)
            graph[firstNode].append(secondNode)
    
    return graph

def qsort(data, opt): # opt : 0 -> ASC, opt : 1 -> DESC
    if len(data) <= 1:
        return data
    
    left, right = list(), list()
    pivot = data[0]
    
    for i in range(1, len(data)):
        if opt == 0 : 
            if data[i] < pivot:
                left.append(data[i])
            else:
                right.append(data[i])
        elif opt == 1:
            if data[i] > pivot:
                left.append(data[i])
            else:
                right.append(data[i])
    return qsort(left, opt) + [pivot] + qsort(right, opt)

def BFS(graph, V):
    if V not in graph:
        return []
    visit, need_visit = list(), list()
    need_visit.append(V)
    
    while need_visit:
        node = need_visit.pop(0)
        if node not in visit:
            visit.append(node)
            need_visit.extend(qsort(graph[node], 0))
    return visit

def DFS(graph, v):
    if V not in graph:
        return []
    visit, need_visit = list(), list()
    need_visit.append(V)
    
    while need_visit:
        node = need_visit.pop()
        if node not in visit:
            visit.append(node)
            need_visit.extend(qsort(graph[node], 1))
    return visit

[N, M, V] = list(map(int, sys.stdin.readline().split(" ")))
graph = dict()
graph = makeGraph(graph, M, N)
print(" ".join(map(str, DFS(graph, V))))
print(" ".join(map(str, BFS(graph, V))))
