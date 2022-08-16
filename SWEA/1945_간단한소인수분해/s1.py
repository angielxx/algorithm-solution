# SWEA 1945 간단한 소인수분해
# 220809

from glob import glob
import sys

sys.stdin = open('input.txt' , 'r')

T = int(input())

def div(number):
    global N
    alpha = 0
    while True:
        if N % number:
            break
        else:
            N /= number
            alpha += 1
    return alpha

for tc in range(1, 10+1):
    N = int(input())

    a, b, c, d, e = div(2), div(3), div(5), div(7), div(11)
    print('#{} {} {} {} {} {}' .format(tc, a, b, c, d, e))