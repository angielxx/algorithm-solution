# 4843_특별한_정렬
# 220811
# 선택 정렬 방법 사용

import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    
    arr = list(map(int, input().split()))
    
    for i in range(N - 1):
        idx = i
        for j in range(i+1, N):
            if i % 2:  # 홀수일 때 : 최소값 찾기
                if arr[idx] > arr[j]:
                    arr[idx], arr[j] =  arr[j], arr[idx]
            else:  # 짝수일 때 : 최대값 찾기
                if arr[idx] < arr[j]:
                    arr[idx], arr[j] =  arr[j], arr[idx]
    
    print('#{}' .format(tc), *[ arr[i] for i in range(10)])