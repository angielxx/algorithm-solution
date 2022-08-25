# SWEA 5097. 회전
# 220825

import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    # N개의 숫자, M번 회전
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    i = 0
    while i < M:
        front = arr.pop(0)
        arr.append(front)
        i += 1

    print('#{}' .format(tc), arr.pop(0))