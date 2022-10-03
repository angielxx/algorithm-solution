# BOJ 1647 도시 분할 계획
# 221003

import collections
import sys
input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())
edge = []
for _ in range(M):
    u, v, w = map(int, input().split())
    edge.append([u, v, w])
edge.sort(key=lambda x: x[2])

rep = [i for i in range(N+1)]

def findset(x):
    while x != rep[x]:
        x = rep[x]
    return x

def union(x, y):
    a, b = findset(x), findset(y)
    if a < b:
        rep[findset(y)] = a
    else:
        rep[findset(x)] = b

cnt = 0
total = 0
MST = []
for u, v, w in edge:
    if findset(u) != findset(v):
        cnt += 1
        union(u,v)
        total += w
        MST.append([u, v, w])
MST.sort(key=lambda x: -x[2])
max_w = MST[0][2]

print(total - max_w)
