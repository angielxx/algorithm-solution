# BOJ 11676 트리의 지름
# 221005

import collections
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

V = int(input())
graph = [[] * (V+1) for _ in range(V+1)]

for _ in range(V):
    Q = collections.deque()
    Q += list(map(int, input().split()))
    # 정점 번호
    u = Q.popleft()
    
    while len(Q) > 1:
        temp = []
        for _ in range(2):
            temp.append(Q.popleft())
        v, w = temp
        graph[u].append([v, w])
        graph[v].append([u, w])

def dfs(start, dist):
    for v, w in graph[start]:
        if distance[v] == -1:
            distance[v] = dist + w
            dfs(v, dist + w)

# 루트에서 제일 먼 노드
distance = [-1] * (V+1)
distance[1] = 0
dfs(1, 0)

start = distance.index(max(distance))
distance = [-1] * (V+1)
distance[start] = 0
dfs(start, 0)

print(max(distance))