# BOJ 1967 트리의 지름
# 221005

import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])
    graph[v].append([u, w])

def dfs(now, dist):
    for v, w in graph[now]:
        # 방문하지 않은 경우
        if distance[v] == -1:
            distance[v] = dist + w
            dfs(v, dist + w)

# 루트에서 제일 먼 곳
distance = [-1] * (n+1)
distance[0] = 1
dfs(1, 0)

# 루트에서 제일 먼 곳에서 제일 먼 노드 찾기
start = distance.index(max(distance))
distance = [-1] * (n+1)
distance[start] = 0
dfs(start, 0)

print(max(distance))