import sys
input = sys.stdin.readline

n = int(input())
top = list(map(int, input().strip().split(' ')))

for i in range(n):
    top[i] = (top[i], i+1)

answer = []

left = []
for i in range(n):
    height, index = top[i]

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