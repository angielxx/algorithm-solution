import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

sum_arr = [0 for _ in range(N + 1)]

for i in range(1, len(sum_arr)):
    sum_arr[i] = sum_arr[i-1] + arr[i-1]

for _ in range(M):
    i, j = map(int, input().split())
    print(sum_arr[j] - sum_arr[i-1])