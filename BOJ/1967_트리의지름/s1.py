# BOJ 1967 트리의 지름
# 220915

import sys
input = sys.stdin.readline

n = int(input())

ch1 = [0] * (n+1)
ch2 = [0] * (n+1)
# 각 간선 가중치를 자식 노드를 인덱스로 저장
arr = [0] * (n+1)

for _ in range(n-1):
    p, c, w = map(int, input().split())
    if not ch1[p]:
        ch1[p] = c
    else:
        ch2[p] = c
    arr[c] = w

# 왼쪽 경로, 오른쪽 경로 중 큰 값을 저장
max_list = [0] * (n+1)
status = [0] * (n+1)

def getMax(n):
    if not ch1[n] and not ch2[n]:
        max_list[n] = 0
        return 0
    else:
        left = right = 0
        if ch1[n]:
            left = getMax(ch1[n]) + arr[ch1[n]]
        if ch2[n]:
            right = getMax(ch2[n]) + arr[ch2[n]]
        max_list[n] = max(left, right)
        return max(left, right)
getMax(1)

# getStatus(n)
for i in range(n+1):
    if not ch1[i] and not ch2[i]:
        status[i] = arr[i]
    else:
        left = right = 0
        if ch1[i]:
            left = arr[ch1[i]] + max_list[ch1[i]]
        if ch2[i]:
            right = arr[ch2[i]] + max_list[ch2[i]]
        status[i] = left + right

print(max(status))