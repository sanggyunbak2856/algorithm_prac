graph = dict()

graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

def DFS(graph, startNode):
    visit, needVisit = list(), list()
    needVisit.append(startNode)
    
    while needVisit:
        node = needVisit.pop()
        if node not in visit:
            visit.append(node)
            needVisit.extend(graph[node])
    
    return visit

print(DFS(graph, 'A'))