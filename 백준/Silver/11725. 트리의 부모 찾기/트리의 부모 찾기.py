# BOJ 11275 트리의 부모 찾기
# 220930

import collections
import sys
input = sys.stdin.readline

N = int(input())
adj = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

P = [0] * (N+1)
Q = collections.deque()
Q.append(1)
while Q:
    root = Q.popleft()
    for v in adj[root]:
        if v != 1 and not P[v]:
            P[v] = root
            Q.append(v)
for i in range(2, N+1):
    print(P[i])
