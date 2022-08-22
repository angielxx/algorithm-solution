# BOJ 2635 수 이어가기
# 220821

import sys
N = int(sys.stdin.readline())

max_combi = []
max_len = 0
for i in range(1, N+1):  # (1, N) : 틀렸습니다.
    combi = [N, i]
    j = 2
    while True:
        num = combi[j-2] - combi[j-1]
        if num < 0:
            break
        combi.append(num)
        j += 1
        if len(combi) >= max_len:   # indent가 안 들어가 있었음
            max_len = len(combi)
            max_combi = combi[:]

print(max_len)
print(*max_combi)