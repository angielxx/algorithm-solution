# SWEA 1225. 암호생성기
# 220824

import sys
sys.stdin = open('input.txt', 'r')

T = 10

for _ in range(1, T+1):
    tc = int(input())
    nums = list(map(int, input().split()))

    i = 1
    while True:
        # print(i)
        # 맨 앞의 원소 삭제
        num = nums.pop(0) - i
        # 맨 뒤에 추가
        nums.append(num)
        if num <= 0:
            nums[-1] = 0
            break
        i = (i + 1) % 5
        if i == 0:
            i = 5

    print('#{}' .format(tc), *nums)