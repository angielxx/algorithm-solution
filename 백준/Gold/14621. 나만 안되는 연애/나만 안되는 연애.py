# BOJ 14621 나만 안되는 연애
# 221019

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
type = [0] + list(input().split())
edge = [list(map(int, input().split())) for _ in range(M)]
edge.sort(key=lambda x: x[2])

rep = [i for i in range(N + 1)]
connected = [0] * (N + 1)

def find_set(x):
    if rep[x] != x:
        rep[x] = find_set(rep[x])
    return rep[x]

def union(x, y):
    a, b = find_set(x), find_set(y)
    if a < b:
        rep[b] = a
    else:
        rep[a] = b

total = 0
cnt = 0
for u, v, d in edge:
    if find_set(u) != find_set(v):
        if type[u] != type[v]:
            total += d
            union(u, v)
            cnt += 1

if cnt == N-1:
    print(total)
else:
    print(-1)