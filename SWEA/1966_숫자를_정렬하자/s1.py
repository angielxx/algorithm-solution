# 1966_숫자를 정렬하자
# 220811

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr = list(map(int, input().split()))

    # 선택 정렬로 정렬해보자. 1 4 7 8 0
    for i in range(N):
        minIdx = i
        # print(i)
        for j in range(i+1, N):
            if arr[minIdx] > arr[j]:
                minIdx = j
        arr[minIdx], arr[i] = arr[i], arr[minIdx]
    
    print('#{}' .format(tc), *arr)
