import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
top = list(map(int, input().strip().split(' ')))
top = deque(top)

for i in range(n):
    top[i] = (top[i], i+1)

answer = []

left = []
while top:
    height, index = top.popleft()

    for i in range(len(left) - 1, -1, -1):
        h, idx = left[i]
        if h >= height:
            answer.append(idx)
            break
    else:
        answer.append(0)
    
    while left and left[-1][0] <= height:
        left.pop()
        
    left.append((height, index))
        
print(*answer)