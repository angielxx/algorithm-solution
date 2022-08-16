# 12712_파리퇴치3
# 220814

import sys
from xml.etree.ElementInclude import XINCLUDE
sys.stdin = open('in1.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    # 2차원 배열 만들기
    # 0의 벽을 M-1만큼 만든다
    arr = []
    for _ in range(M-1):
        arr.append([0] * ( N + (M-1) * 2))
    for _ in range(N):
        arr.append([0] * (M-1) + list(map(int, input().split())) + [0] * (M-1))
    for _ in range(M-1):
        arr.append([0] * ( N + (M-1) * 2))

    # + : 상하좌우
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    # x : 왼쪽 상단부터 시계방향
    xi = [-1, -1, 1, 1]
    xj = [-1, 1, -1, 1]

    # 파리의 합의 최댓값
    max = 0

    for i in range(M-1, N + (M-1)):
        for j in range(M-1, N + (M-1)):
            # + 방향 분사 총합
            s1 = 0
            s1 += arr[i][j] 
            # X 방향 분사 총합
            s2 = 0
            s2 += arr[i][j]
            for k in range(1, M):
                # s1 구하기
                s1 += arr[i + di[0] * k][j + dj[0] * k]
                s1 += arr[i + di[1] * k][j + dj[1] * k]
                s1 += arr[i + di[2] * k][j + dj[2] * k]
                s1 += arr[i + di[3] * k][j + dj[3] * k]
                # s2 구하기
                s2 += arr[i + xi[0] * k][j + xj[0] * k]
                s2 += arr[i + xi[1] * k][j + xj[1] * k]
                s2 += arr[i + xi[2] * k][j + xj[2] * k]
                s2 += arr[i + xi[3] * k][j + xj[3] * k]
            if s1 >= max:
                max = s1
            if s2 >= max:
                max = s2

    print('#{} {}' .format(tc, max))