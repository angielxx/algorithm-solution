W, H = map(int, input().split())

# 시계방향의 전체 획의 상점과 경비원 위치 저장할 리스트
# 꼭짓점은 마지막 빼고 제외
clock = [0] * ( (W + H) * 2 )

N = int(input())
# 상점 위치 저장
# 각 획이 꼭짓점 제외하고 1부터 시작하므로,
# 상점 위치 인덱스는 -1 해줘야함

# 위치 저장 함수
def save_position(P, idx, n):
    if P == 1:
        clock[idx] = n
    # 2, 3일 때는 거꾸로 저장
    elif P == 2:
        clock[(W-1) + H + (W-1) - idx ] = n  # 8,16  
    elif P == 3:
        clock[(W-1) + H + (W-1) + H - idx ] = n  # 2, 
    elif P == 4:
        clock[W + idx] = n # 4, 13

for n in range(1, N+1):
    P, I = map(int, input().split())

    idx = I - 1
    save_position(P, idx, n)

# 경비원 위치 저장
P, I = map(int, input().split())
save_position(P, I-1, 'A')


# 경비원 기준으로 재정렬
idx = clock.index('A')
route = clock[idx:] + clock[0:idx]

sum = 0
# 상점까지 최단거리 구하기
for n in range(1, N+1):
    # 시계방향 거리
    d1 = route.index(n)
    # 반시계방향 거리
    d2 = len(route) - d1
    if d1 > d2:
        sum += d2
    else:
        sum += d1

print(sum)