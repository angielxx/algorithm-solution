import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split(' '))
target = deque(list(map(int, input().split(' '))))

q = deque([i for i in range(1, n+1)])

answer = 0
while target:
    if target[0] == q[0]:
        q.popleft()
        target.popleft()
        continue
    
    idx = q.index(target[0])
    if idx < len(q) - idx:
        q.append(q.popleft())
        answer += 1
    else:
        q.appendleft(q.pop())
        answer += 1

print(answer)
