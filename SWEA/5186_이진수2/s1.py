# SWEA 5186 이진수2
# 220920

import sys
sys.stdin = open('sample_input.txt', 'r')

def len(string):
    length = 0
    for s in string:
        length += 1
    return length

T = int(input())
for tc in range(1, T+1):
    N = float(input())

    result = ''
    status = True
    for i in range(1, 50):
        if N == 0:
            break
        if N >= 2**(-(i)):
            result += '1'
            N -= 2**(-(i))
        else:
            result += '0'

    if len(result) < 13:
        print('#{}' .format(tc), result)
    else:
        print('#{}' .format(tc), 'overflow')
