# SWEA 1265 달란트2
# 220913

# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, P = map(int, input().split())
    
    dummy = N // P
    rest = N % P

    dums = [dummy] * P
    for i in range(rest):
        dums[i] = dums[i] + 1
    
    result = dums[0]
    for i in range(1, P):
        result *= dums[i]
    print('#{}' .format(tc), result)