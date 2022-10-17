# BOJ 6497 전력난
# 221017

import sys
input = sys.stdin.readline

def find_set(x):
    while x != rep[x]:
        x = rep[x]
    return x

def union(x, y):
    rep[max(find_set(x), find_set(y))] = min(find_set(x), find_set(y))

while True:
    # 집의 수, 길의 수
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break

    # u, v, w
    edge = [list(map(int, input().split())) for _ in range(n)]
    edge.sort(key=lambda x: x[2])

    # 현재 비용
    current_total = 0
    for i in range(n):
        current_total += edge[i][2]

    # 대표 원소
    rep = [i for i in range(m+1)]

    total = 0
    for u, v, w in edge:
        if find_set(u) != find_set(v):
            union(u, v)
            total += w

    print(current_total - total)