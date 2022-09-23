N = int(input())

positions = list()
for n in range(N):
    x, y = map(int, input().split())
    for i in range( x, x + 10):
        for j in range(y, y+10):
            positions.append((i, j))

area = set(positions)

print(len(area))