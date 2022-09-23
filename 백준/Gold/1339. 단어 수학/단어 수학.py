import collections

N = int(input())

nums = [input() for _ in range(N)]

d = collections.defaultdict(int)
for i in range(len(nums)):
    num = list(nums[i])
    k = 0
    while num:
        alpha = num.pop()
        d[alpha] += 10**k
        k += 1

alnum = sorted(list(d.items()), key=lambda x: -x[1])

n = 9
result = 0
for i in range(len(alnum)):
    alpha, num = alnum[i]
    result += num*n
    n -= 1
print(result)