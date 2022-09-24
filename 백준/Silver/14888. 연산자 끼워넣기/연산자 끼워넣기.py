# BOJ 14888 연산자 끼워넣기
# 220924

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

# 0 1 2 3
# +, -, *, /
opt_li = list(map(int, input().split()))
opt = [0]*(opt_li[0]) + [1] * (opt_li[1]) + [2] * (opt_li[2]) + [3] * (opt_li[3])
# print('opt', opt)

max_result = float('-inf')
min_result = float('inf')

def dfs(idx, subset=[]):
    global max_result
    global min_result

    if len(subset) == N-1:
        # print('subset', subset)
        # 계산하기
        temp = arr[:]
        num1 = temp.pop(0)
        # print('temp', temp)
        for i in range(len(subset)):
            idx = subset[i]
            # print('num1',num1)
            # print(temp[i])
            if opt[idx] == 0:
                num1 += temp[i]            
            elif opt[idx] == 1:
                num1 -= temp[i]            
            elif opt[idx] == 2:
                num1 *= temp[i]            
            elif opt[idx] == 3:
                if num1 < 0 and temp[i] > 0:
                    num1 = -((-(num1)) // temp[i])
                else:
                    num1 = num1 // temp[i]
        # print(num1)
        if num1 > max_result:
            max_result = num1
        if num1 < min_result:
            min_result = num1
        return
    
    # print(subset)
    # dfs 계속
    for i in range(N-1):
        if i in subset:
            continue
        dfs(i, subset + [i])

# dfs 시작
for i in range(N-1):
    dfs(i, [i])

print(max_result)
print(min_result)