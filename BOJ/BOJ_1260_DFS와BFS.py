# BOJ_1260_DFS와 BFS
# 220815

"""
DFS > 깊이 탐색
BFS > 넓이 탐색

1
2
"""
import sys

# 정점의 개수, 간선의 개수, 탐색을 시작할 정점의 번호
N, M, V = map(int, sys.stdin.readline().split())

graph = { i: [] for i in range(1, N+1) }

# 간선 정보 받아서 저장
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    graph[i].append(j)
    graph[j].append(i)

# 정렬
for i in range(1, N+1):
    graph[i] = sorted(graph[i])

def dfs(V, discovered=[]):
    discovered.append(V)
    for w in graph[V]:
        if w not in discovered:
            discovered = dfs(w, discovered)
    return discovered

def bfs(V):
    discovered =[V]
    queue = [V]
    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                queue.append(w)
    return discovered

print(*dfs(V))
print(*bfs(V))