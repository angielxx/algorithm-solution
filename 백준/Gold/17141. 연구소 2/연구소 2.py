import collections
import copy
from pprint import pprint

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

virus = []
check = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            virus.append((i, j))
        else:
            check.append((i, j))

delta = [[1,0],[-1,0],[0,1],[0,-1]]
min_depth = float('inf')

# 바이러스 퍼뜨리는 bfs
# 모든 지점에서 동시에 시작하도록 한번에 queue에 넣어주기 -> x
def bfs(subset):
    queue = collections.deque()
    queue.extend(subset)
    depth = 0

    # 바이러스 표시할 temp
    temp = [[0] * N for _ in range(N)]
    # 벽이거나 바이러스 놓은 곳이면 '-'으로 바꾸기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                temp[i][j] = '-'

    # 방문표시
    visited = [[0] * N for _ in range(N)]
    while queue and depth <= min_depth:
        for _ in range(len(queue)):
            si, sj = queue.popleft()

            for k in range(4):
                ni, nj = si + delta[k][0], sj + delta[k][1]
                if (ni, nj) not in subset and 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != 1 and visited[ni][nj] == 0:
                    queue.append((ni, nj))
                    temp[ni][nj] = temp[si][sj] + 1
                    depth = temp[ni][nj]
                    visited[ni][nj] = 1
    # print(subset)
    # pprint(temp)
    # print(depth)
    # print()
    return temp, depth

# 부분집합 만드는 dfs
def dfs(idx, subset=[]):
    global min_depth

    if len(subset) == M:
        # 바이러스 퍼트리기
        # print(subset)
        temp, depth = bfs(subset)
        status = True
        for i in range(N):
            for j in range(N):
                if temp[i][j] == '-':
                    continue
                if (i, j) not in subset and temp[i][j] == 0:
                    status = False
        if status:
            # print('hey')
            # print()
            # print()
            if depth < min_depth:
                min_depth = depth
        return

    for i in range(idx+1, len(virus)):
        x, y = virus[i]
        dfs(i, subset + [(x, y)])

# 부분집합 만들기
for i in range(len(virus)):
    x, y = virus[i]
    dfs(i, [(x, y)])

if min_depth == float('inf'):
    print(-1)
else:
    print(min_depth)