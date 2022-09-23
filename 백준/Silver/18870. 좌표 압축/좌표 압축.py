
import sys
N = int(sys.stdin.readline())

arr1 = list(map(int, sys.stdin.readline().split()))

arr2 = list(sorted(set(arr1)))
dict = { arr2[i] : i for i in range(len(arr2))}

for i in arr1:
    print(dict[i], end=' ')