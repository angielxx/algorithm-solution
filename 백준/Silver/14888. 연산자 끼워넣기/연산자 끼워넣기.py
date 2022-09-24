# BOJ 14888 연산자 끼워넣기
# 220924

import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))

maximum = float('-inf')
minimum = float('inf')

def dfs(depth, total, plus, minus, mult, div):
    global maximum
    global minimum

    if depth == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    if plus:
        dfs(depth+1, total + num[depth], plus-1, minus, mult, div)
    if minus:
        dfs(depth+1, total - num[depth], plus, minus-1, mult, div)
    if mult:
        dfs(depth+1, total * num[depth], plus, minus, mult-1, div)
    if div:
        if total < 0 and num[depth] > 0:
            total = -((-(total)) // num[depth])
        else:
            total = total // num[depth]
        dfs(depth+1, total, plus, minus, mult, div-1)

dfs(1, num[0], op[0], op[1], op[2], op[3])
print(maximum)
print(minimum)