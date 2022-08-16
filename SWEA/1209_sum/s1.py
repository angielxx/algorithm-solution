# SWEA 1209 sum
# 220810

import sys

sys.stdin = open('input.txt' , 'r')

T = 10

for tc in range(1, T+1):
    # 테케 번호
    tc = int(input())
    # 행의 값 받아서 2차원 배열 생성
    arr = [ list(map(int, input().split())) for _ in range(100) ]
    
    # 최댓값 초기값
    max_sum = 0

    # 행의 합
    for i in range(100):
        sum_i = 0 # 각 행의 합
        for j in range(100):
            sum_i += arr[i][j]
        if sum_i >= max_sum:
            max_sum = sum_i

    # 열의 합
    for j in range(100):
        sum_j = 0
        for i in range(100):
            sum_j += arr[i][j]
        if sum_j >= max_sum:
            max_sum = sum_j

    # 대각선의 합
    # 00 11 22 ... 99 99
    # 99 0  -> 더한게 99
    sum_X = 0
    for i in range(100):
        sum_X += arr[i][i]
    if sum_X >= max_sum:
        max_sum = sum_X

    sum_Y = 0
    for i in range(100):
        sum_Y += arr[i][100 - i - 1]
    if sum_Y >= max_sum:
        max_sum = sum_Y
    
    print('#{} {}' .format(tc, max_sum))