import sys
input = sys.stdin.readline

"""
막대기 시작할 때 총 갯수 += 1, 현재막대기 갯수 += 1
레이저 쏠 때마다 총 갯수 += 현재막대기 갯수
"""

ss = input().strip()

answer = 0
stack = []

i = 0
while i < len(ss):
    s = ss[i]
    if s == '(' and ss[i+1] == ')':
        answer += len(stack)
        i += 2
        continue
    elif s == '(':
        stack.append('(')
        answer += 1
    elif s == ')':
        stack.pop()
    i += 1
    
print(answer)