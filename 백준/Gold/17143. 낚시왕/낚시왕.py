import sys
from copy import deepcopy
from collections import defaultdict
input = sys.stdin.readline

h, w, m = map(int, input().split()) # 행, 열, 상어
arr = [[-1] * w for _ in range(h)] # -1 : 아무것도 없는 상태
sharks = defaultdict(list)

for i in range(m):
    r,c,s,d,z = map(int, input().split())
    sharks[i] = [r-1,c-1,s,d,z] # 행, 열, 속력, 방향, 크기
    arr[r-1][c-1] = (i, z) # 번호, 크기

"""
사람위치 = n초 <= c
상어 위치 = 큐
두개 이상의 칸 

함수
상어 이동
상어
번호 = (r, c, s, d, z)
지도[r-1][c-1] = 상어번호
"""
# _ 위, 아래, 오른쪽, 왼쪽
di = ['x', -1, 1, 0, 0]
dj = ['x', 0, 0, 1, -1]

def changeDir(d):
    if d == 1: return 2
    if d == 2: return 1
    if d == 3: return 4
    if d == 4: return 3

def move(i, j, s, d, num):
    for _ in range(s):
        i += di[d]
        j += dj[d]
        
        if i < 0 or i >= h or j < 0 or j >= w:
            if i < 0: i += 2
            if i >= h: i -= 2
            if j < 0: j += 2
            if j >= w: j -= 2
            d = changeDir(d)
            sharks[num][3] = d
    return (i, j)

people = -1
caught = 0
while people < w - 1:
    people += 1
    temp = [[-1] * w for _ in range(h)]
    sharks_to_kill = [] # 'dictionary changed size during iteration' 방지
    
    # print('people', people)
    # print(caught)
    # for key, val in sharks.items():
    #     print(key, val)
    # print()
    # for a in arr:
    #     print(a)

    
    # 잡을 수 있는 상어 탐색
    for i in range(h):
        if arr[i][people] != -1:
            shark_num = arr[i][people][0]
            caught += arr[i][people][1]
            # print('caught!!', shark_num, arr[i][people][1])
            sharks.pop(shark_num)
            break # 땅과 가장 가까운 상어 잡고 중단
    # 상어 이동
    for key, val in sharks.items():
        i,j,s,d,z = val
        
        ni, nj = move(i, j, s, d, key)
        # 이동한 곳에 상어가 있을 때
        if temp[ni][nj] != -1:
            num, size = temp[ni][nj]
            win = num if size > z else key
            lose = key if size > z else num
            temp[ni][nj] = (win, sharks[win][4]) # 이긴 상어로
            sharks_to_kill.append(lose)
            sharks[win][0] = ni
            sharks[win][1] = nj
        else:
            temp[ni][nj] = (key, z)
            sharks[key][0] = ni
            sharks[key][1] = nj
            
    for num in sharks_to_kill:
        sharks.pop(num)
    # print()
    # for a in temp:
    #     print(a)
    # print()
    # print()
    # print()
    arr = deepcopy(temp)

print(caught)