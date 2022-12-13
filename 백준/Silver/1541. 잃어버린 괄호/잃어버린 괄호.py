import sys
input = sys.stdin.readline

arr = input().strip().split('-')
numbers = []

for i in range(len(arr)):
    numbers.append(sum(list(map(int, arr[i].split('+')))))

total = numbers[0]
for i in range(1, len(numbers)):
    total -= numbers[i]

print(total)