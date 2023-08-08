import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    test = input().strip()
    
    left = deque([])
    right = deque([])
    
    for i in range(len(test)):
        s = test[i]
        if s == '<':
            if left: right.appendleft(left.pop())
        elif s == '>':
            if right: left.append(right.popleft())
        elif s == '-':
            if left: left.pop()
        else:
            left.append(s)
    print(''.join(left) + ''.join(right))