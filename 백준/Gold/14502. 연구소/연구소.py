import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

# 세로, 가로
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

virus = []
empty = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            empty.append((i, j))
        elif graph[i][j] == 2:
            virus.append((i, j))

def chooseWall(arr, cnt):
    result = []
    if cnt == 0:
        return [[]]

    for i in range(len(arr)):
        el = arr[i]
        rest  = chooseWall(arr[i + 1:], cnt - 1)
        for r in rest:
            result.append([el] + r)
    return result

answer = 0

def bfs(wall):
    global answer
    
    arr = deepcopy(graph)
    for i, j in wall:
        arr[i][j] = 1
    
    q = deque(virus)
    
    while q:
        si, sj = q.popleft()
        for k in range(4):
            ni = si + di[k]
            nj = sj + dj[k]
            if ni < 0 or ni >= n or nj < 0 or nj >= m or arr[ni][nj] != 0:
                continue
            arr[ni][nj] = 2
            q.append((ni, nj))
    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                cnt += 1
    if cnt > answer:
        answer = cnt

for wall in chooseWall(empty, 3):
    bfs(wall)

print(answer)