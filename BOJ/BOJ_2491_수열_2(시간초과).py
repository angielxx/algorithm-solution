# BOJ 2491_수열
# 220818

import sys

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

# 방향이 같으면 스택에 넣고, 다르면 길이 비교하여 최대값이면 저장, 스택 초기화와 i되돌아가기
stack = []
i = 0
dir1, dir2 = 0, 0
max = 0
idx = 0
# 맨 마지막 원소를 확인할 때까지 반복
while i < N:
    if stack:
        # 방향 구하기
        if num[i] == stack[-1]:
            dir2 = dir1
        elif num[i] > stack[-1]:
            dir2 = 1
        elif num[i] < stack[-1]:
            dir2 = -1

        # 방향 비교
        if len(stack) == 2 and dir1 == 0:
            dir1 = dir2
        if dir1 == dir2 or dir2 == 0:
            stack.append(num[i])
            # idx 찾기
            if num[i] != num[i - 1]:
                idx = i
            i += 1
        elif dir1 != dir2:
            cnt = len(stack)
            if cnt > max:
                max = cnt
            stack.clear()
            i = idx

    else:
        stack.append(num[i])
        if num[i] > num[i+1]:
            dir1 = -1
        elif num[i] < num[i+1]:
            dir1 = 1
        else:
            dir1 = 0
        i += 1

print(max)
