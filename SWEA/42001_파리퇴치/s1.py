# 42001_파리퇴치
# 220811

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    # 2차원 배열로 바로 저장
    arr = [ list(map(int, input().split())) for _ in range(N) ]

    # 모든 합을 저장할 리스트
    sum_list = list()

    for i in range(N - M + 1):  # 첫칸의 행번호 # i : 0,1,2,3
        for j in range(N - M + 1):  # 첫칸의 열번호 # i : 0,1,2,3
            sub_sum = 0
            for k in range(M):  # j : 0,1 (증가값)
                for l in range(M):
                    sub_sum += arr[i + k][j + l]
            sum_list.append(sub_sum)

    max_sum = 0
    for sum in sum_list:
        if max_sum < sum:
            max_sum = sum

    print('#{} {}' .format(tc, max_sum))
        