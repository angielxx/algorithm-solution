# SWEA 5102. 노드의 거리
# 220825

import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    # V : 노드 개수, E : 간선 개수
    V, E = map(int, input().split())
    # 노드 개수만큼 인접 리스트 생성
    # 0번부터 V번까지 (0번은 없는 노드)
    adj = [[] for _ in range(V+1)]
    visited = [0] * (V + 1)

    for _ in range(E):
        # 간선정보
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
    # print(adj)
    # 출발노드, 도착노드
    S, G = map(int, input().split())

    # BFS
    q = [S]
    visited[S] = 1

    while q:
        # print(q)
        # print(visited)
        v = q.pop(0)
        if v == G:
            break
        for w in adj[v]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[v] + 1

    result = visited[G]-1
    print('#{}' .format(tc), result)

