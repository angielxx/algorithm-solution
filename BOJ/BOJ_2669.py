# 인풋값으로 직사각형의 영역좌표(x,y)들을 담는 리스트 만들기
# 1*1 정사각형의 왼쪽 아래 좌표만 담는다(정사각형 하나 세는 기준)
area = list()
for _ in range(4):
    a, b, c, d = map(int, input().split())
    for i in range(a, c): # 1~4
        for j in range(b, d): # 2,4
            area.append((i, j))

# 이차원리스트는 셋트로 변환이 안된다....
# 리스트 안에 튜플을 담은 형태로 변경!
# 세트로 변환하여 중복되는 좌표 삭제
new_area = set(area)
# 전체 넓이 = 좌표의 갯수
print(len(new_area))