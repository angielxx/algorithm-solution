# SWEA 달팽이숫자 복습
# 220827

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    # N*N 배열 생성
    arr = [[0]*N for _ in range(N)]

    # 우하좌상 이동
    # dir 0 1 2 3 = 우 하 좌 상
    move = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    # 숫자 배치
    dir = 0
    si = sj = 0
    for num in range(1, N*N+1):
        # 현재 위치 숫자 배치
        arr[si][sj] = num
        # 다음 숫자 위치 찾기
        ni, nj = si + move[dir][0], sj + move[dir][1]

        # 유효성 검사
        if ni < 0 or nj < 0 or ni >= N or nj >= N or arr[ni][nj] != 0:
            # 이동한만큼 빼고
            ni -= move[dir][0]
            nj -= move[dir][1]

            # 방향 전환
            dir = (dir + 1) % 4
            ni += move[dir][0]
            nj += move[dir][1]
        # 다음 위치 설정
        si, sj = ni, nj

    print('#{}' .format(tc))
    for i in range(N):
        print(*arr[i])
