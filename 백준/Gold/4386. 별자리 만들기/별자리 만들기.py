# BOJ 4386 별자리 만들기
# 221003

import math
import sys
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
arr = [list(map(float, input().split())) for _ in range(n)]

edge = []
for i in range(n-1):
    x1, y1 = arr[i]
    for j in range(i, n):
        x2, y2 = arr[j]
        dist = math.sqrt(abs(x1-x2)**2 + abs(y1-y2)**2)
        edge.append([i, j, dist])
edge.sort(key=lambda x: x[2])

rep = [i for i in range(n+1)]

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
for u, v, dist in edge:
    if findset(u) != findset(v):
        cnt += 1
        total += dist
        union(u, v)
        if cnt == n:
            break
print(round(total, 2))