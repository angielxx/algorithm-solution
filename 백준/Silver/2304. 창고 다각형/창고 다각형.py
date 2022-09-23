N = int(input())

# 기둥들의 정보 받아 저장 [ (), (), ...]
position_list = list()
for n in range(N):
    x, y = map(int, input().split())
    position_list.append((x, y))
 
# x기준으로 정렬
position_list.sort()

# 젤 높은 기둥 찾기
highest_idx = 0
highest = position_list[0][1]
for i in range(N):
    if position_list[i][1] > highest:
        highest = position_list[i][1]
        highest_idx = i
    else:
        pass

# 왼 -> 오
total = 0
x1, y1 = position_list[0]
for i in range(highest_idx + 1): #
    if position_list[i][1] >= y1:
        height = y1
        width = position_list[i][0] - x1
        total += width * height
        x1, y1 = position_list[i]
    else:
        pass

# 오 -> 왼
a1 , b1 = position_list[-1]
for i in range(N - 1, highest_idx - 1, -1):
    if position_list[i][1] >= b1:
        height = b1
        width = a1 - position_list[i][0]
        total += width * height
        a1, b1 = position_list[i]
    else:
        pass

total += highest
print(total)