import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

def cutTrees(h):
    total = 0
    for i in trees:
        if i >= mid:
            total += i - h
    return total

s = 1
e = max(trees)
answer = 0
# s == e이면 절단 높이를 찾게됨
while s <= e:
    mid = (s + e) // 2

    if cutTrees(mid) >= M:
        s = mid + 1
    else:
        e = mid - 1
print(e)