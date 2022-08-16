# SWEA 6485 삼성시의 버스 노선
# 220809

import sys

sys.stdin = open('s_input.txt' , 'r')

T = int(input())

for tc in range(1, T+1):
    # 노선 개수
    N = int(input())

    # 전체 버스정류장 리스트
    route = [0] * 5001
    # 각 노선이 다니는 정류장 번호에 +1
    for i in range(N):
        # 각 노선에 대해 A부터 B까지 번호 저장
        A, B = map(int, input().split())
        for i in range(A, B+1):
            route[i] += 1
    
    # 정류장 개수
    P = int(input())

    # 정류장 번호 저장
    stop_list = [ int(input()) for _ in range(P) ]

    print('#{}' .format(tc), end=' ')
    for stop_idx in stop_list:
        print(route[stop_idx], end=' ')
