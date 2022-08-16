# 1210_Ladder1
# 220811

import sys

sys.stdin = open('input.txt', 'r')

for _ in range(10):
    tc = int(input())

    # 양쪽에 0이 벽 생성해서 2차원 배열 만들기 (index 에러 방지)
    arr = list()
    for _ in range(100):
        arr.append( [0] + list(map(int, input().split())) + [0] )

    # 도착지점 찾기
    cj = 0
    for j in range(1,101):
        if arr[99][j] == 2:
            cj = j
            break
        else:
            continue

    ci = 99
    while ci > 0:
        if arr[ci][cj - 1]: # 좌가 있다면 이동
            while arr[ci][cj - 1] == 1:
                cj -= 1
            ci -= 1
        elif arr[ci][cj + 1]:  # 우가 있다면 이동
            while arr[ci][cj + 1] == 1:
                cj += 1
            ci -= 1
        else: # 양쪽에 없으면 위로 이동
            ci -= 1
    result = cj - 1
    print('#{} {}' .format(tc, result))