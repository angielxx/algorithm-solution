# BOJ 9372 상근이의 여행
# 220929

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())

    adj = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    visited = [0] * (N+1)
    def dfs(start, cnt):

        visited[start] = 1

        # 인접 노드 탐색
        for v in adj[start]:
            if visited[v] == 0:
                cnt = dfs(v, cnt + 1)
        return cnt
            
    result = dfs(1, 0)
    print(result)