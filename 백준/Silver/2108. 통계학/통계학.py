import sys
from collections import Counter
input = sys.stdin.readline

# 수의 개수
N = int(input())
# 숫자들
numbers = [ int(input()) for _ in range(N)]

# 오름차순 정렬
numbers.sort()
# print(numbers)

# 리스트 합계, 평균
total = sum(numbers)
average = round(total / len(numbers))

# 중앙값
mid_idx = len(numbers) // 2
middle = numbers[mid_idx]

# 최빈값
most_common = Counter(numbers).most_common()
common = 0
if len(most_common) == 1:
    common = most_common[0][0]
else: 
    if most_common[0][1] == most_common[1][1]:
        common = most_common[1][0]
    else:
        common = most_common[0][0]

# 범위
gap = numbers[-1] - numbers[0]

print(average)
print(middle)
print(common)
print(gap)