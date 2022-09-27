# BOJ 18405 경쟁적 전염
# 220927

import collections
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# S초 뒤, (X, Y)에 바이러스가 있는지 확인
S, X, Y = map(int, input().split())

queue = []
for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            queue.append((arr[i][j], 0, i, j))
queue.sort()
queue = collections.deque(queue)

delta = [[1,0],[-1,0],[0,1],[0,-1]]
while queue:
    virus, s, i, j = queue.popleft()
    if s == S:
        break
    for k in range(4):
        ni, nj = i + delta[k][0], j + delta[k][1]
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
            arr[ni][nj] = virus
            queue.append((virus, s + 1, ni, nj))

print(arr[X-1][Y-1])