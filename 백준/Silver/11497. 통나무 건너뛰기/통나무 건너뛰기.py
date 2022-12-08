import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    arr2 = [0] * N
    mid = N // 2
    arr2[mid] = arr[-1]

    left, right = mid - 1, mid + 1
    i = N - 2
    while i >= 0:
        arr2[left] = arr[i]
        if i - 1 >= 0:
            arr2[right] = arr[i - 1]
        i -= 2
        left -= 1
        right += 1
    # print('arr', arr2)

    MAX = 0
    for i in range(N-1):
        # print('gap', arr2[i], arr2[i+1])
        gap = abs(arr2[i] - arr2[i+1])
        if gap > MAX: MAX = gap
    print(MAX)