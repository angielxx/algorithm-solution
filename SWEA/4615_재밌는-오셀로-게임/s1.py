# SWEA 4615 재밌는 오셀로 게임
# 220920

import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

def oslo(i, j, color):
    me = 'B' if color == 1 else 'W'
    enemy = 'W' if color == 1 else 'B'
    arr[i][j] = me
 
    # 왼쪽 위 대각선방향부터 시계방향 델타탐색
    delta = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]

    for k in range(8):
        si, sj = i, j
        # 바꿀 적 돌의 위치
        toChange = []
        while True:
            ni, nj = si+delta[k][0], sj+delta[k][1]
            if 0 <= ni < N and 0 <= nj < N:
                # 0 나오면 바로 중단
                if arr[ni][nj] == 0:
                    break
                # 적이 나오면 바꿀 적의 돌 추가
                if arr[ni][nj] == enemy:
                    toChange.append((ni, nj))
                # 나 자신이 나오면 저장해놨던 바꿀 적의 돌 바꾸기
                elif arr[ni][nj] == me:
                    # toChange가 없으면 나 자신 다음에 바로 나 자신이 나온 것
                    if toChange:
                        for ci, cj in toChange:
                            arr[ci][cj] = me
                    # 나 자신이 한번 나온 곳 까지만 바꿀 수 있기 때문에 바꾸고 나면 바로 그 방향에 대한 탐색 중단
                    break
            else:
                break
            si, sj = ni, nj

for tc in range(1,T+1):
    N, M = map(int, input().split())

    arr = [[0]*N for _ in range(N)]
    # 초기 흑돌, 백돌 놓기
    arr[N//2-1][N//2-1] = arr[N//2][N//2] = 'W'
    arr[N//2][N//2-1] = arr[N//2-1][N//2] = 'B'

    for _ in range(M):
        j, i, color = map(int, input().split())
        i -= 1
        j -= 1
        oslo(i, j, color)

    # 최종 흑돌, 백돌 수 세기
    B_cnt = W_cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'B':
                B_cnt += 1
            elif arr[i][j] == 'W':
                W_cnt += 1

    print('#{}' .format(tc), B_cnt, W_cnt)