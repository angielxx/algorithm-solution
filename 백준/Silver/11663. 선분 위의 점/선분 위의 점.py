n, m = map(int, input().split(' '))

dots = sorted(map(int, input().split(' ')))

answer = []

for _ in range(m):
    line_s, line_e = map(int, input().split(' '))
    
    si, ei = 0, n - 1
    
    range_s, range_e = 0, 0
    
    # 길이 스타트 인덱스 찾기
    while si <= ei:
        mi = (si + ei) // 2
        
        if dots[mi] < line_s:
            si = mi + 1
        else:
            ei = mi - 1
    
    range_s = ei + 1

    si, ei = 0, n - 1
    
    while si <= ei:
        mi = (si + ei) // 2
        
        if line_e < dots[mi]:
            ei = mi - 1
        else:
            si = mi + 1
    
    range_e = ei
        
    answer.append(range_e - range_s + 1)
    
for a in answer:
    print(a)