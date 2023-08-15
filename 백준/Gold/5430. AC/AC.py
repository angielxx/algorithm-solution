import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    p = input().strip()
    n = int(input())
    arr_input = input().strip()[1:-1]
    arr = deque(arr_input.split(',')) if arr_input else deque()

    direct = 1 # 1이면 정방향, -1이면 역방향
    for s in p:
        if s == 'R':
            direct *= -1
        else:
            if not arr:
                print('error')
                break
            else:
                if direct == 1: arr.popleft()
                else: arr.pop()
    else:         
        arr = list(arr)
        if direct == -1:
            arr = arr[::-1]
        print('[', end='')
        print(','.join(arr), end='')
        print(']')