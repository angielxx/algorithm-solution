# BOJ 1504 특정한 최단 경로
# 220930

import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

N, E = map(int, input().split())

graph = [[] for _ in range(N+1)]

# 그래프 양방향으로 저장
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

# 반드시 거쳐야하는 정점
V1, V2 = map(int, input().split())

def dijkstra(start):
    Q = []
    heapq.heappush(Q, (0, start))
    distance = [INF] * (N+1)
    distance[start] = 0

    while Q:
        w, v = heapq.heappop(Q)

        # 거리테이블과 비교하여 더 크면 무시
        if distance[v] < w:
            continue

        # 선택한 노드와 인접한 노드 확인
        for dist, next in graph[v]:
            cost = w + dist
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(Q, (cost, next))
    return distance

from_root = dijkstra(1)
from_V1 = dijkstra(V1)
from_V2 = dijkstra(V2)

answer1 = from_root[V1] + from_V1[V2] + from_V2[N]
answer2 = from_root[V2] + from_V2[V1] + from_V1[N]
fin = min(answer1, answer2)
print(fin if fin < INF else -1)