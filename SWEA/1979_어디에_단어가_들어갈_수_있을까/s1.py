# 1979_어디에_단어가_들어갈_수_있을까
# 220811

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

def count(arr):
    total = 0

    for i in range(N):  # i번째 행
        # 연속된 1세기
        cnt = 0
        j = 0  # j번째 열
        while j < N:
            # 1이면 cnt += 1
            # 0이면 확인하고 초기화
            if arr[i][j] == 1:
                cnt += 1
                if j == N-1 and cnt == K:
                    total += 1
            else:
                if cnt == K:
                    total += 1
                    cnt = 0
                else:
                    cnt = 0
            j += 1
    return total

for tc in range(1, T+1):
    N, K = map(int, input().split())

    # 퍼즐 생성
    arr = [ list(map(int, input().split())) for _ in range(N) ]
    
    # 90도 돌리기
    new_arr = [ [0] * N for _ in range(N) ]
    for i in range(N):
        for j in range(N):
            new_arr[i][j] = arr[N - j - 1][i]

    result = count(arr) + count(new_arr)
    print('#{} {}' .format(tc, result))