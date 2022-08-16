a, b = map(int, input().split())
if a % b == 0:
    print('B')
elif a % b == 1:
    print('A')
elif a % b == 2:
    print('B')