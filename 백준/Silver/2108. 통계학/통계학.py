import sys
input = sys.stdin.readline

N = int(input())
# 각 정수들의 빈도를 저장할 배열
#  -4000 ~ 0 ~ 4000
counts = [0 for i in range(8001)]

sum = 0
for i in range(N):
    # 정수 받기
    n = int(input())
    sum += n
    # 빈도 체크
    counts[n+4000] += 1

# 평균
print(round(sum/N))

# 중앙값
run = 0
i = -1
# (N+1) // 2 는 중앙에 위치하는 값의 차례 (~번째)
while run < (N+1) // 2:
    # counts가 0~8000
    # counts 배열에서 몇번째 위치하는지 세는 것 = 값 + 4000인것
    i += 1
    # 빈도가 0 이상인 숫자들을 작은 것 부터 세게 됨
    run += counts[i]
print(i - 4000)

# 최빈값
m = max(counts)
maxs = []
for i in range(8001):
    if counts[i] == m:
        maxs.append(i - 4000)
if len(maxs) > 1:
    print(maxs[1])
else:
    print(maxs[0])

# 범위
MAX = 4000
# counts배열의 8000번째 원소부터 쭉 내려오면서 본다
# counts[MAX+4000]이 0보다 크면 최대값인 것
while not counts[MAX+4000]:
    MAX -= 1

MIN = -4000
# 최솟값은 0번째 원소부터 쭉 올라오면서 본다
while not counts[MIN+4000]:
    MIN += 1
print(MAX - MIN)