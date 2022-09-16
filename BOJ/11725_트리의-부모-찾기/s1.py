# BOJ 11275 트리의 부모 찾기
# 220914

import sys
input = sys.stdin.readline

# 노드의 개수
N = int(input())

# 입력값 저장
arr = [list(map(int, input().split())) for _ in range(N-1)]

# 인덱스를 자식 노드로 부모 노드 저장
par = [0] * (N+1)

# 루트 1부터 처리
p, c = 0, 0
for i in range(N-1):
    a, b = arr[i]
    # a가 루트 1인 경우
    if a == 1:
        p, c = a, b
    # b가 루트 1인 경우
    elif b == 1:
        c, p = a, b
    par[c] = p

for i in range(N-1):
    a, b = arr[i]
    # 1이 있는 경우 패스
    if a == 1 or b == 1:
        pass
    else:
        # 부모가 이미 있으면
        if par[a]:
            p, c = a, b
        elif not par[a]:
            c, p = a, b
        par[c] = p

for i in range(2, N+1):
    print(par[i])