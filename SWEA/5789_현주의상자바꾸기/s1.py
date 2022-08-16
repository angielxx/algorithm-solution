# SWEA 5789 현주의 상자 바꾸기
# 220809

import sys

sys.stdin = open('sample_input.txt' , 'r')

T = int(input())

for tc in range(1, T+1):
    N, Q = map(int, input().split())
    
    # 길이가 N인 리스트 만들기
    arr = [0] * N

    # Q회 반복하여 상자의 숫자 변경
    for i in range(1, Q+1):
        L, R = map(int, input().split())

        # L, R은 실제 인덱스 번호보다 1 크므로 1씩 빼주어 range에 넣는다
        for idx in range(L - 1, R):
            arr[idx] = i
        print(arr)

    print('#{}' .format(tc), *arr)