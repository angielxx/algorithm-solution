# SWEA 5185 이진수
# 220920

import sys
sys.stdin = open('sample_input.txt', 'r')

def len(num):
    length = 0
    for n in num:
        length += 1
    return length

T = int(input())
for tc in range(1, T+1):
    N, hex = input().split()
    N = int(N)

    length = N*4

    # 16진수 > 10진수 > 2진수
    dec = int('0x'+hex, 16)
    binary = bin(dec)[2:]
    
    result = '0' * (N*4 - len(binary)) + binary
    print('#{}' .format(tc), result)

    