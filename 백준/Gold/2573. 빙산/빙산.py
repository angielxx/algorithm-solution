# pypy3 56%에서 시간초과

import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().strip().split(' '))
arr = [list(map(int, input().strip().split(' '))) for _ in range(n)]

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

year = 0
while True:
    temp = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[0 for _ in range(m)] for _ in range(n)]
    
    def bfs(i, j):
        q = deque([(i, j)])
        visited[i][j] = 1
        while q:
            si, sj = q.popleft()
            cnt = 0
            for k in range(4):
                ni = si + di[k]
                nj = sj + dj[k]
                if 0 <= ni < n and 0 <= nj < m:
                    if arr[ni][nj] == 0:
                        cnt += 1
                    elif not visited[ni][nj] and arr[ni][nj] != 0:
                        q.append((ni, nj))
                        visited[ni][nj] = 1
            temp[si][sj] = max(arr[si][sj] - cnt, 0)
        return

    cnt = 0
    flag = False
    s = 0
    for i in range(n):
        if flag: break
        for j in range(m):
            s += arr[i][j]
            if arr[i][j] and visited[i][j] == 0:
                cnt += 1
                bfs(i, j)
            if cnt > 1:
                flag = True
                break

    if not s:
        year = 0
        break
            
    if cnt > 1:
        break
    else:
        arr = temp
        year += 1
    
print(year)