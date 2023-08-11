import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)][::-1]

answer = 0

stack = []
for i in range(n):
    h = arr[i]

    while stack and arr[stack[-1]] < h:
        stack.pop()
     
    if not stack:
        answer += i
    else:
        answer += i - stack[-1] - 1
    
    stack.append(i)

print(answer)