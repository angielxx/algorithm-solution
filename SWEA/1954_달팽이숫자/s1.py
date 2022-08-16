# SWEA 1954 달팽이 숫자
# 220810

import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    # i, j의 증가값을 저장하는 리스트
    di = []
    dj = []

    # 규칙에 따라 증가값
    for n in range(N, 0, -1): # 4,3,2,1
        for _ in range(n):
            di.append(0)
            dj.append(1 - (2) * ((N - n) % 2))
        for _ in range(n-1):
            di.append(1 - (2) * ((N - n) % 2))
            dj.append(0)

    # N * N 2차원 배열 만들기
    arr = [ [0] * N for _ in range(N)]
    # 1~N*N 까지 순서대로 di, dj를 행과 열 번호에 더해가며 2차원 배열에 넣기
    i = j = 0
    for n in range(1, N * N + 1):
        # 1은 무조건 0,0
        if n == 1:
            arr[i][j] = 1
        else:
            i += di[n - 1]
            j += dj[n - 1]
            arr[i][j] = n

    print('#{}' .format(tc))
    
    # 행 순서대로 출력
    for list in arr:
        print(*list)