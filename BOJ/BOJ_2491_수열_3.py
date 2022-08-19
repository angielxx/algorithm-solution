# BOJ 2491_수열
# 220818

# 풀이 참고

import sys

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

inc = [0] * N
dec = [0] * N

max = 0
for i in range(N):
    if i == 0:
        inc[i], dec[i] = 1,1
    else:
        if num[i-1] < num[i]:
            inc[i] = inc[i-1] + 1
            dec[i] = 1
        elif num[i-1] > num[i]:
            inc[i] = 1
            dec[i] = dec[i-1] + 1
        else:
            inc[i] = inc[i - 1] + 1
            dec[i] = dec[i - 1] + 1
    # max체크
    if dec[i] > max:
        max = dec[i]
    if inc[i] > max:
        max = inc[i]

print(max)