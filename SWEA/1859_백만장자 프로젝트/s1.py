# SWEA 1859. 백만 장자 프로젝트
# 220816

# Fail (Runtime error)!

"""
1 1 3 1 2 > 3일 때 파는게 가장 이득 : 5
1 1 2 1 3 > 3일 때 파는게 가장 이득 : 7
1 1 3 2 1
전체 리스트
max_idx 구하기
max_idx가 0이 아니면 진행, 0이면 0출력
max_idx까지 이득 += (최고가 - 자기자신), 자기자신은 popleft
max_idx도 popleft
전체 리스트 업데이트 됨! 다시 처음부터 반복
종료

popleft를 하면 idx가 계속 줄어드니까 주의
"""

import sys
import collections
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    # 데크로 선언
    days = collections.deque()
    for num in map(int, input().split()):
        days.append(num)

    # 최종 이득
    margin = 0

    while True:
        # 가격이 제일 큰 날 찾기
        max_idx, max_val = 0, 0
        for i in range(N):
            if days[i] >= max_val:
                max_val = days[i]
                max_idx = i

        if max_idx == 0:
            break
        else:
            for j in range(max_idx):
                margin += (max_val - days[j])
            for _ in range(max_idx + 1):
                days.popleft()
                N -= 1

    print('#{} {}' .format(tc, margin))