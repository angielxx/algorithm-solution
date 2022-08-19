# BOJ 2559 수열
# 220819
# 투포인터, 슬라이딩 윈도우

N, K = map(int, input().split())

li = list(map(int, input().split()))

# 0  1  2  3 4 5 6  7 8  9
# 3 -2 -4 -9 0 3 7 13 8 -3
max = 0
for i in range(N-K+1):
    s = 0
    for j in range(K):
        s += li[i+j]
    if s >= max:
        max = s

print(max)