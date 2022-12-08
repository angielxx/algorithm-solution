# 투포인터 사용
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
x = int(input())

arr.sort()

left, right = 0, n - 1

cnt = 0
while left < right:
    s = arr[left] + arr[right]
    if s == x : cnt += 1
    # 큰 경우 right - 1
    if s > x:
        right -= 1
    # 작거나 같은 경우
    else:
        left += 1
print(cnt)
    