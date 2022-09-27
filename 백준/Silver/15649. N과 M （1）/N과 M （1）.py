# BOJ 15649
# 220927

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num = [i for i in range(1, N+1)]

# 수열 만들기
def bfs(start, subset=[]):
    if len(subset) == M:
        print(*subset)
        return
    for i in range(1, N+1):
        if i not in subset:
            bfs(i, subset + [i])
    pass

# 수열 만들기 시작
for i in num:
    bfs(i, [i])