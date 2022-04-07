import sys
import copy

def makeGraph(graph, M, N):
    for i in range(N*N):
        graph[i] = [i]
    for i in range(N): # 기준 : i * 3
        for j in range(N): # offset
            if M[i][j] == 0: # 0인 경우 pass
                continue
            node = i * N + j
            if M[i][j] == 1:
                graph[node].append(node)
            if i != 0 and M[i-1][j] == 1: # 위 확인
                graph[node].append((i - 1) * N + j)
            if i != N-1 and M[i+1][j] == 1: # 아래 확인
                graph[node].append((i + 1) * N + j)
            if j != N-1 and M[i][j+1] == 1: # 오른족 확인
                graph[node].append(i * N + j + 1)
            if j != 0 and M[i][j-1] == 1: # 왼쪽 확인
                graph[node].append(i * N + j - 1)
    
    return graph

def BFS(graph, start):
    if len(graph[start]) <= 1:
        return 0
    
    visit, need_visit = list(), list()
    need_visit.append(start)
    
    while need_visit:
        node = need_visit.pop(0)
        if node not in visit:
            copiedValue = copy.deepcopy(graph[node])
            visit.append(node)
            need_visit.extend(copiedValue)
            del graph[node]
    return len(visit)

N = int(sys.stdin.readline())
M = [[i for i in list(map(int, sys.stdin.readline().split("\n")[0]))] for _ in range(N)]
graph = dict()
graph = makeGraph(graph, M, N)
num = []

for i in range(N*N):
    if i in graph:
        n = BFS(graph, i)
    else:
        n = 0
    if n == 0:
        continue
    num.append(n)

num.sort()
print(len(num))
for i in range(len(num)):
    print(num[i])

# 1. 지도 크기, 지도 입력
# 2. 그래프 만들기
# 3. BFS로 단지 내 아파트 개수 파악
##### 그래프 만들기 #####
# 그래프는 딕셔너리로 생성함
# 그래프 키들의 값은 리스트
# 각 경계를 확인하고 위 아래 오른쪽 왼쪽이 1이면 그래프 값 리스트에 append
# 값의 리스트 길이가 1이면 지도상에서 0임, 
# 단지 내 아파트가 하나라면 리스트에 자기 자신을 또 추가 (길이 : 2)
##### 단지 내 아파트 개수 파악 #####
# BFS로 파악
# 딕셔너리에서 한번 방문한 아파트의 키를 삭제함
# BFS로 단지 내 아파트의 개수를 파악할 때 그래프 딕셔너리에 키가 존재하는지 확인
