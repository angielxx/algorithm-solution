# BOJ 1339 단어수학
# 220920

N = int(input())
nums = [input() for _ in range(N)]

arr = []
for i in range(N):
    num = list(nums[i])
    k = 0
    while num:
        arr.append((10**k, num.pop()))
        k += 1

arr.sort()
# 인덱스를 숫자로, 값을 알파벳으로 저장
numbers = [0] * 10

# 9부터 역순으로 arr에서 가장 큰 자릿수를 가진 숫자부터
# 9~0의 숫자를 배정
n = 9
while arr and n >= 0:
    num, alpha = arr.pop()
    if alpha not in numbers:
        numbers[n] = alpha
        n -= 1

result = 0
for i in range(N):
    num = list(nums[i])[::-1]
    for idx, alpha in enumerate(num):
        result += (10**idx) * numbers.index(alpha)

print(result)