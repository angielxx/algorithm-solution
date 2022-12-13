import sys
input = sys.stdin.readline

N = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

total = 0
MIN = price[0]

for i in range(N - 1):
    if price[i] < MIN:
        MIN = price[i]
    total += MIN * distance[i]

print(total)