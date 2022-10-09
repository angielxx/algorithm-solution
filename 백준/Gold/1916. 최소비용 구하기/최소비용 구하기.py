# BOJ 1916 최소비용 구하기
# 221009

import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

S, E = map(int, input().split())


Q = []
heapq.heappush(Q, (0, S))
distance = [INF] * (N + 1)
distance[S] = 0

while Q:
    weight, now = heapq.heappop(Q)
    if weight > distance[now]:
        continue

    if now == E:
        break
    
    for dist, next in graph[now]:
        cost = distance[now] + dist
        if cost < distance[next]:
            distance[next] = cost
            heapq.heappush(Q, (cost, next))

print(distance[E])