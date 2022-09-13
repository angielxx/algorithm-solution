# SWEA 1861 정사각형방
# 220913

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    # N*N
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    depth = [[0]*N for _ in range(N)]

    # 델타 : 상하좌우
    delta = [[-1,0],[1,0],[0,-1],[0,1]]

    def getDepth(i, j):
        si, sj = i, j
        depth = 1
        while True:
            for k in range(4):
                ni, nj = si + delta[k][0], sj + delta[k][1]
                if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == arr[si][sj] + 1:
                    depth += 1
                    si, sj = ni, nj
                    break
            else:
                break
        return depth

    max_depth = -1
    room_num = N**2 + 1
    for i in range(N):
        for j in range(N):
            depth[i][j] = getDepth(i, j)
            if depth[i][j] > max_depth:
                max_depth = depth[i][j]
                room_num = arr[i][j]
            elif depth[i][j] == max_depth:
                if arr[i][j] < room_num:
                    room_num = arr[i][j]
   
    # print(depth)
    print('#{}' .format(tc), room_num, max_depth)