# BOJ 1339 단어수학
# 220921

import collections
import sys

N = int(input())

nums = [input() for _ in range(N)]

arr = []
for i in range(N):
    num = list(nums[i])
    k = 0
    while num:
        n = num.pop()
        arr.append((10**k, n))
        k += 1

arr.sort(key=lambda tuple: -tuple[0])
print(arr)
num_dict = collections.defaultdict(int)

n = 9
i = 0
while i < len(arr) and n >= 0:
    _, alpha = arr[i]
    if alpha in num_dict.keys():
        pass
    else:
        num_dict[alpha] = n
        n -= 1
    i += 1
print(num_dict.get)
result = 0
for i in range(len(arr)):
    num, alpha = arr[i]
    result += num * num_dict[alpha]

print(result)