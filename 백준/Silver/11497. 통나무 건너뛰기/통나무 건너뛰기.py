import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    result = 0
    # 인덱스가 2 차이나게 두어야함
    for i in range(2, N):
        result = max(result, abs(arr[i] - arr[i-2]))
    print(result)