# BOJ 7576 토마토
# 221013

import collections
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
arr = [ list(map(int, input().split())) for _ in range(N)]

Q = collections.deque()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            Q.append([(i, j), 0])

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

if len(Q) != M*N:
    max_time = 0
    while Q:
        position, time = Q.popleft()
        x, y = position
        if time > max_time:
            max_time = time

        for k in range(4):
            nx, ny = x + di[k], y + dj[k]
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0:
                Q.append([(nx, ny), time + 1])
                arr[nx][ny] = 1

    flag = True
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                flag = False
    if flag:
        print(max_time)
    else:
        print(-1)
else:
    print(0)