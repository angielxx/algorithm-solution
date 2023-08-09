import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
target = deque([int(input()) for _ in range(n)])

numbers = deque([i for i in range(1, n+1)])

stack = []
result = []
answer = []
while target:
    if not stack:
        stack.append(numbers.popleft())
        answer.append('+')
        continue
        
    if stack[-1] == target[0]:
        result.append(stack.pop())
        target.popleft()
        answer.append('-')
    elif stack[-1] != target[0] and numbers:
        stack.append(numbers.popleft())
        answer.append('+')
    else:
        print('NO')
        break
else:
    for a in answer:
        print(a)
        