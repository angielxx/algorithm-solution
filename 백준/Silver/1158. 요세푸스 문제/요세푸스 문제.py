import sys
input = sys.stdin.readline

n, k = map(int, input().split(' '))

arr = [i + 1 for i in range(n)]

i = -1
answer = []
while arr:
    i =  (i + k) % len(arr)
    answer.append(arr[i])
    arr = arr[:i] + arr[i+1:]
    i -= 1
    
print('<',end='')
for i in range(len(answer)):
    if i == len(answer) - 1:
        print(answer[i], end='')
    else:
        print(answer[i], end=', ')
print('>')