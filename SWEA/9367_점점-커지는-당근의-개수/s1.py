# 9367_점점-커지는-당근의-개수
# 220812

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))

    # 연속할 때 카운트
    # 최소 1번은 연속하므로 초기값은 1
    max = 1

    cnt = 1
    for i in range(N):
        # 마지막 숫자라면 다음 숫자 안 보고 cnt값 바로 비교
        if i == N - 1:
            if cnt >= max:
                max = cnt

        # 마지막 숫자가 아니라면
        elif i < N - 1:
            # 다음 숫자를 보고 
            # 연속하는 숫자면 카운트 1업한 뒤 다음 숫자로 넘어간다.
            if num[i] + 1 == num[i+1]:
                cnt += 1
            # 연속하는 숫자가 아니라면 카운트 값 비교하고 카운트 초기화한다.
            else:
                if cnt >= max:
                    max = cnt
                cnt = 1
    print('#{} {}' .format(tc, max))