import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().strip().split()))[::-1]

answer = [-1] * n

stack = []
for i in range(n):
    num = arr[i]

    while stack and arr[stack[-1]] <= num:
        stack.pop()
        
    if stack:
        answer[i] = arr[stack[-1]]
        
    stack.append(i)

print(*answer[::-1])