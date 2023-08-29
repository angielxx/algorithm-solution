import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

# 세로, 가로
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

virus = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            virus.append((i, j))

answer = 0

def bfs(graph):
    global answer
    
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    
    q = deque(virus)
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if ni < 0 or ni >= n or nj < 0 or nj >= m or graph[ni][nj] != 0:
                continue
            graph[ni][nj] = 2
            q.append((ni, nj))
            
    cnt  = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                cnt += 1
    if cnt > answer:
        answer = cnt

def makeWall(cnt, graph):
    if cnt == 3:
        bfs(graph)
        return
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                makeWall(cnt + 1, deepcopy(graph))
                graph[i][j] = 0

makeWall(0, arr)
print(answer)