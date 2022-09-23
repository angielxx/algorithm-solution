area = list()
for _ in range(4):
    a, b, c, d = map(int, input().split())
    for i in range(a, c): # 1~4
        for j in range(b, d): # 2,4
            area.append((i, j))
new_area = set(area)
print(len(new_area))