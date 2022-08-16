# 4836_색칠하기
# 220811

import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    # 2차원 배열 만들기
    arr = [ [0] * 10 for _ in range(10) ]

    for _ in range(N):
        i1, j1, i2, j2, color = map(int, input().split())

        # 영역 색칠하기
        for i in range(i1, i2 + 1):
            for j in range(j1, j2 + 1):
                # 같은 색인 영역은 겹치지 않는다고 했으므로 1씩 더한 뒤, 2인 곳이 보라색
                arr[i][j] += 1

        # 보라색인 칸 세기
        cnt = 0
        for i in range(10):
            for j in range(10):
                if arr[i][j] == 2:
                    cnt += 1

    print('#{} {}' .format(tc, cnt))

