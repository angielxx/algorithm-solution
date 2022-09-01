# BOJ 1946 신입사원
# 220830

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    score = [list(map(int, input().split())) for _ in range(N)]
    check = [ True ] * N

    cnt = 0
    for i in range(N-1):
        a, b = score[i]
        for j in range(i+1, N):
            c, d = score[j]
            if a > c:
                if b < d:
                    # 헷갈리지 않게
                    check[i], check[j] = True, True
                else:
                    check[i] = False
            elif a < c:
                if b > d:
                    check[i], check[j]
                else:
                    check[j] = False
    print(check.count(True))