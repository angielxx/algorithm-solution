# 9386_연속한-1의-개수
# 220812

import sys
sys.stdin = open('input1.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    bin = input()

    # 1이 연속한 최댓값을 저장
    max = 0
    for i in range(N): # 0 ~ 9 1111
        cnt = 0
        # 1을 만나면 카운트 시작 (첫번째 1)
        if bin[i] == '1':
            cnt += 1

            # 마지막 숫자가 아니면 다음 숫자를 본다.
            if i < N - 1:
                j = 1
                # i + j가 마지막 숫자일 때까지만 다음 숫자를 확인
                while i + j < N:
                    if bin[i + j] == '1':
                        cnt += 1
                        j += 1
                    else:
                        break
                if cnt >= max:
                    max = cnt
                    cnt = 0
            
            # 마지막 숫자라면 cnt 비교
            else:
                if cnt >= max:
                    max = cnt

    print('#{} {}' .format(tc, max))
