# SWEA 고대유적 복습
# 220827

import sys
sys.stdin = open('input1.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_length = 0
    # 행 탐색
    for i in range(M):
        # 연속된 1의 길이
        cnt = 0
        for j in range(N):
            if arr[i][j] == 1:
                cnt += 1
            else:
                if cnt > max_length:
                    max_length = cnt
                cnt = 0
            if cnt > max_length:
                max_length = cnt
    # 열 탐색
    for j in range(N):
        cnt = 0
        for i in range(M):
            if arr[i][j] == 1:
                cnt += 1
            else:
                if cnt > max_length:
                    max_length = cnt
                cnt = 0
            if cnt > max_length:
                max_length = cnt


    print('#{} {}' .format(tc, max_length))
