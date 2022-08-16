N = int(input())
num = list(map(int, input().split(' ')))
num.sort()
index = (N-1)//2

print(num[index])