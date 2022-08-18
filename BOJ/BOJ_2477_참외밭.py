# BOJ 2477 참외밭
# 220818

import sys

# 1미터에 자라는 참외 개수
N = int(sys.stdin.readline())

direction = []
length = []
for _ in range(6):
    a, b = map(int, sys.stdin.readline().split())
    direction.append(a)
    length.append(b)

length = length * 2
direction = direction * 2

for i in range(12):
    if direction[i] == direction[i+2]:
        w_idx1, w_idx2 = i, i+2
        break

w1 = length[w_idx1]
w2 = length[w_idx2]

if w_idx1 == 0:
    h1 = length[-1]
else:
    h1 = length[w_idx1 - 1]
if w_idx2 == 11:
    h2 = length[1]
else:
    h2 = length[w_idx2 + 1]

area = (w1 * h1 + w2 * h2) * N
print(area)