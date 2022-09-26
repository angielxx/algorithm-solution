# BOJ 16234 인구이동
# 220926

import collections
import sys
input = sys.stdin.readline

N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

delta = [[0,1],[0,-1],[1,0],[-1,0]]

def bfs(i, j):

    queue = collections.deque()
    queue.append((i, j))
    
    union = []
    country = 0
    population = 0
    while queue:
        si, sj = queue.popleft()
        visited[si][sj] = 1
        country += 1
        population += arr[si][sj]
        if (si, sj) not in union:
            union.append((si, sj))
        else:
            continue
        
        for k in range(4):
            ni, nj = si + delta[k][0], sj + delta[k][1]
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and L <= abs(arr[ni][nj] - arr[si][sj]) <= R:
                queue.append((ni, nj))
    return union

days = 0
while True:
    visited = [[0] * N for _ in range(N)]
    status = False
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 1
                union = bfs(i, j)
                if len(union) > 1:
                    status = True
                    average = sum([arr[x][y] for x, y in union]) // len(union)
                    for x, y in union:
                        arr[x][y] = average
    if not status:
        break
    days += 1
print(days)