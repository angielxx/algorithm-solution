# SWEA 파리퇴치3 복습
# 220827

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    # M길이만큼의 벽 사방에 만들기
    arr = []
    for _ in range(M):
        arr.append([0]*(N + M*2))
    for _ in range(N):
        arr.append([0]*M + list(map(int, input().split())) + [0]*M)
    for _ in range(M):
        arr.append([0]*(N + M*2))

    # 십자 방향, 상하좌우
    cross = [[-1,0], [1,0], [0, -1], [0, 1]]
    # 엑스 방향, 좌상부터 시계방향
    x = [[-1,-1], [-1, 1], [1, 1], [1, -1]]
    # print(arr)
    # 최대값 저장
    max_sum = 0
    for i in range(M, N+M):
        for j in range(M, N+M):
            # arr[i][j]가 중심인 파리퇴치 영역에 대한 합
            s1, s2 = 0, 0
            s1 += arr[i][j]
            s2 += arr[i][j]
            # 영역의 박스들 위치값
            # 각 방향의 합 구하기
            for k in range(1, M):
                for di, dj in cross:
                    a, b = i + di*k, j + dj*k
                    s1 += arr[a][b]
                    # print(s1)
                for ni, nj in x:
                    c, d = i + ni*k, j + nj*k
                    s2 += arr[c][d]
            if s1 > max_sum:
                max_sum = s1
            if s2 > max_sum:
                max_sum = s2
            # print(s1, s2)
    print('#{} {}' .format(tc, max_sum))