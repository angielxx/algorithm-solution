from collections import deque
import sys
inf = sys.maxsize

def solution(n, roads, sources, destination):
    dist = [-1 for _ in range(n+1)]
    dist[destination] = 0
    graph = [[] for _ in range(n+1)]
    
    for road in roads:
        a, b = road
        graph[a].append(b)
        graph[b].append(a)
    
    q = deque([destination]) # [위치, 거리, 경로]
    visited = [0 for _ in range(n+1)]
    visited[destination] = 1
    while q:
        now = q.popleft()

        for v in graph[now]:
            if visited[v] == 0:
                dist[v] = dist[now] + 1
                visited[v] = 1
                q.append(v)

    return list(dist[s] for s in sources)