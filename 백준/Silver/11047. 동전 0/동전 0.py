import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = []
for i in range(N):
    coin = int(input())
    if coin <= K:
        coins.append(coin)
coins.sort(reverse=True)

cnt = 0
for i in range(len(coins)):
    if K == 0:
        break
    else:
        cnt += K // coins[i]
        K -= coins[i] * (K//coins[i])

print(cnt)