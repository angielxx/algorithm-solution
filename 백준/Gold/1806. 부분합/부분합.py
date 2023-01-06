import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))

flag = False
left = right = total = cnt = 0
result = N

while True:
  if total >= S:
    flag = True
    result = min(result, cnt)
    total -= arr[left]
    left += 1
    cnt -= 1
  elif right == N:
    break
  else:
    total += arr[right]
    right += 1
    cnt += 1

if flag:
  print(result)
else:
  print(0)