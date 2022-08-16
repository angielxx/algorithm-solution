# BOJ_18870_좌표압축
# 220814

import sys
N = int(sys.stdin.readline())

arr1 = list(map(int, sys.stdin.readline().split()))

# no_repeat = list()
# for i in range(N):
#     if no_repeat.count(arr[i]) == 0:  -> count : O(N)
#         no_repeat.append(arr[i])

# no_repeat.sort()                      -> sort : O(N) or O(n log n)

arr2 = list(sorted(set(arr1)))
dict = { arr2[i] : i for i in range(len(arr2))}

for i in arr1:
    print(dict[i], end=' ')