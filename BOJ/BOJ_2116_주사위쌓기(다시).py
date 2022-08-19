# BOJ 2116 주사위 쌓기
# 220819

import sys

# 케이스별로 옆면의 인덱스 세팅
idxA = [1, 2, 3, 4]
idxB = [0, 2, 4, 5]
idxC = [0, 1, 3, 5]

# 주사위 개수
N = int(sys.stdin.readline())
# 주사위 정보
dice = []

for _ in range(N):
    dice.append(list(map(int, sys.stdin.readline().split())))

max_sum = 0
# 각 위아랫면이 A-F, B-D, C-E일 때 최대합
sumA, sumB, sumC = 0, 0, 0
# 각 케이스의 옆면을 리스트에 넣고 최대값을 각 케이스의 합의 변수에 저장
for i in range(N):
    # 각 주사위 i마다 리스트를 새로 초기화하여 선언해야함
    sideA, sideB, sideC = [], [], []
    # # 각 케이스별로 옆면이 될 수 있는 숫자 넣기
    for j in idxA:
        sideA.append(dice[i][j])
    for j in idxB:
        sideB.append(dice[i][j])
    for j in idxC:
        sideC.append(dice[i][j])

    sumA += max(sideA)
    sumB += max(sideB)
    sumC += max(sideC)
print(sumA, sumB, sumC)
if sumA > max_sum:
    max_sum = sumA
elif sumB > max_sum:
    max_sum = sumB
elif sumC > max_sum:
    max_sum = sumC

print(max_sum)