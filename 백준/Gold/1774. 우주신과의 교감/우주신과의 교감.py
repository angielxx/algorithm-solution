# BOJ 1774 우주신과의 교감
# 221003

import math
import sys
input = sys.stdin.readline

def findset(x):
    if rep[x] == x:
        return x
    else:
        rep[x] = findset(rep[x])
        return rep[x]

def union(x, y):
    a, b = findset(x), findset(y)
    if a < b:
        rep[findset(y)] = a
    else:
        rep[findset(x)] = b

N, M = map(int, input().split())
# 모든 좌표
arr = [0] + [list(map(int, input().split())) for _ in range(N)] # coordinate

# 대표원소
rep = [i for i in range(N+1)] # par

for _ in range(M):
    u, v = map(int, input().split())
    union(u, v)

# 탐색해야할 경로 저장
edge = []
for i in range(1, N):
    x1, y1 = arr[i]
    for j in range(i+1, N+1):
        x2, y2 = arr[j]
        w = math.sqrt(abs(x1-x2)**2 + abs(y1-y2)**2)
        edge.append([i, j, w])
edge.sort(key=lambda x:x[2])

total = 0
for u, v, w in edge:
    if findset(u) != findset(v):
        total += w
        union(u, v)
        # 모든 정점이 MST에 포함되면 중단

print("{:.2f}".format(total))