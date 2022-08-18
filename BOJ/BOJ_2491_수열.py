# BOJ 2491_수열
# 220818

import sys

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

stack = []
max = 0
# 숫자가 달라지는 순간
i, idx = 0, 0
dir1, dir2 = 0, 0
while i < N:
    print(i, stack)
    # 스택에 원소가 하나라도 있으면 방향 비교
    if stack:
        temp = 1 if stack[-1] < num[i] else -1
        temp = 0 if stack[-1] == num[i] else temp

        # idx 계산
        if temp != 0:
            idx = i
        print(dir1, temp)
        # 1개 있을 때 넣으려고 하는 원소랑 비교하여 초기 방향을 설정
        if len(stack) == 1:
            print('1')
            dir1 = temp
            stack.append(num[i])
            i += 1
        # 2개 이상 있으면, 두번째 방향을 계산하여 dir1과 비교
        # 방향 같으면 스택에 넣고, 다르면 cnt 비교 후 stack, cnt 초기화
        else:
            dir2 = temp
            # 방향이 같은 경우 계속 스택에 넣음
            if dir1 == 0:
                stack.append(num[i])
                i += 1
                dir1 = dir1
            else:
                if dir1 == dir2 or dir2 == 0:
                    print('2')
                    stack.append(num[i])
                    i += 1
                    dir1 = dir2
                # 방향이 달라지면
                elif dir1 != dir2:
                    print('here')
                    cnt = len(stack)
                    if cnt > max:
                        print('4')
                        max = cnt
                        stack.clear()
                        i = idx
    # 스택에 원소가 없으면 넣기만
    else:
        stack.append(num[i])
        i += 1
print(max)