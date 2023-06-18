# 경우의 수
# 1. 각자 이동하는 경우
# 2. 합승
# 2-1. S - A - B
# 2-2. S - B - A
# 계산 순서
# 1 경우 계산
# 2 경우 계산 : S - A와 S - B를 비교
### S - A가 작다면, 2-1
### S - B가 작다면, 2-2
import heapq
import sys
INF = sys.maxsize

def solution(n, s, a, b, fares):
    # print(n, s, a, b)
    weight = [ [0 for _ in range(n + 1)] for _ in range(n + 1)] # i, j = i - j 요금
    graph = [[] for _ in range(n+1)]
    for start, end, w in fares:
        weight[start][end] = w
        weight[end][start] = w
        graph[start].append(end)
        graph[end].append(start)
    
    def way(s,e):
        table = [INF] * (n + 1)
        q = []
        heapq.heappush(q, (0, s))  # fare, now
        table[s] = 0

        while q:
            fare, now = heapq.heappop(q)
            
            if table[now] < fare:
                continue
            if now == e:
                continue
                
            for v in graph[now]:
                w = weight[now][v]
                new_fare = fare + w
                if new_fare < table[v]:
                    table[v] = new_fare
                    heapq.heappush(q, (new_fare, v))
        # print(table)
        # print(table[e])
        return table[e]
    
    answer = []
    for i in range(1, n+1):
        answer.append(way(s, i) + way(i, a) + way(i, b))
    print(answer)
    return min(answer)