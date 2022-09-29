# BOJ 1197 최소 스패닝 트리
# 220929


import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**5)

# 정점의 개수, 간선의 개수
V, E = map(int, input().split())

# 대표원소
rep = [i for i in range(V+1)]

edge = []
for _ in range(E):
    u, v, w = map(int, input().split())
    edge.append([u, v, w])
edge.sort(key=lambda x: x[2])

def find_set(x):
    while x!=rep[x]:
        x = rep[x]
    return x

def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x < y:
        rep[y] = x
    else:
        rep[x] = y
    return

cnt = 0
total = 0
for u, v, w in edge:
    if find_set(u) != find_set(v):
        # cnt += 1
        union(u, v)
        total += w
        # if cnt == V:
        #     break
print(total)