# BOJ 2527_직사각형
# 220818

for i in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    x_cnt = 0
    for i in range(x1, p1 + 1):
        if x2 <= i <= p2:
            x_cnt += 1

    y_cnt = 0
    for i in range(y1, q1 + 1):
        if y2 <= i <= q2:
            y_cnt += 1

    if x_cnt >= 2 and y_cnt >= 2:
        print('a')
    elif x_cnt >= 2 or y_cnt >= 2:
        print('b')
    elif x_cnt == 1 and y_cnt == 1:
        print('c')
    else:
        print('d')
