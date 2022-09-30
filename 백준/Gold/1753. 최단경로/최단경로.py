# BOJ 1753 최단경로
# 220930

import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

# 정점의 개수, 간선의 개수
V, E = map(int, input().split())
# 시작 정점
K = int(input())

graph = [[] for _ in range(V+1)]
distance = [INF] * (V+1)

for _ in range(E):
    u, v, w = map(int, input().split())
    # 가중치를 기준으로 우선순위가 결정되므로 w가 튜플의 첫번째 원소여야함
    graph[u].append((w, v))

def dijkstra(start):
    q=[]
    # 시작노드
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        # 최단 거리가 짧은 노드 꺼내기
        dist, now = heapq.heappop(q)

        # 현재 테이블과 비교하여 가중치가 더 큰 노드면 무시
        if distance[now] < dist:
            continue

        # 선택된 노드와 인접한 노드 확인
        for w, next in graph[now]:
            cost = dist + w
            # 선택된 노드를 거쳐서 이동하는 것이 더 빠른 경우
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(q, (cost, next))

dijkstra(K)
for i in range(1, V+1):
    if i == K:
        print(0)
    elif distance[i] == INF:
        print('INF')
    else:
        print(distance[i])