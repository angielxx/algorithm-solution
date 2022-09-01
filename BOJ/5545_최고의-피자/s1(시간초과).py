# BOJ 5545. 최고의 피자
# 220828

# 토핑의 종류의 수
N = int(input())
# 도우의 가격, 토핑의 가격
A, B = map(int, input().split())
# 도우의 열량
C = int(input())
# N개의 토핑의 열량
toppings = [int(input()) for _ in range(N)]

max_cal = 0
for i in range(1<<N):
    price = A
    cal = C
    choice = []
    for j in range(N):
        if i & (1<<j):
            price += B
            cal += toppings[j]
    result = int(cal / price)
    if result > max_cal:
        max_cal = result

print(max_cal)