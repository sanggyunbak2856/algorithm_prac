import sys

def BFS(graph, start):
    visit, need_visit = list(), list()
    need_visit.append(start)
    
    while need_visit:
        node = need_visit.pop(0)
        if node not in visit:
            visit.append(node)
            need_visit.extend(graph[node])
    
    return visit

def makeGraph(graph, N, M):
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
    
    
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = dict()
graph = makeGraph(graph, N, M)
print(len(BFS(graph, 1)) - 1)
