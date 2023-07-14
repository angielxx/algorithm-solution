import heapq
import sys
inf = sys.maxsize

def solution(N, road, K):
    
    graph = [[] for _ in range(N+1)]
    
    for r in road:
        a, b, c = r
        graph[a].append((c, b)) # (시간, 연결노드)
        graph[b].append((c, a))
    
    distance = [inf for _ in range(N+1)]
    distance[1] = 0
    
    def dijkstra(start):
        q = []
        heapq.heappush(q, (0, start))

        while q:
            time, now = heapq.heappop(q)
            
            if distance[now] < time:
                continue
                
            for w, v in graph[now]:
                cost = time + w
                if distance[v] > cost:
                    distance[v] = cost
                    heapq.heappush(q, (cost, v))
    
    dijkstra(1)
    
    answer = 0
    for i in range(1, N+1):
        if distance[i] <= K:
            answer += 1
    return answer