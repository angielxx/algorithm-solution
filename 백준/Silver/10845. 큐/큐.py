import sys
input = sys.stdin.readline
from collections import deque

N = int(input())

Q = deque()

def push(Q, x):
    Q.append(x)
def pop(Q):
    if len(Q): print(Q.popleft())
    else: print(-1)
def size(Q):
    print(len(Q))
def empty(Q):
    if len(Q): print(0)
    else: print(1)
def front(Q):
    if len(Q): print(Q[0])
    else: print(-1)
def back(Q):
    if len(Q): print(Q[-1])
    else: print(-1)

for _ in range(N):
    command = input()
    if command.startswith('push'):
        x = int(command.split()[-1])
        push(Q, x)
    if command.startswith('pop'):
        pop(Q)
    if command.startswith('size'):
        size(Q)
    if command.startswith('empty'):
        empty(Q)
    if command.startswith('front'):
        front(Q)
    if command.startswith('back'):
        back(Q)