# SWEA 5102. 노드의 거리
# 220825

# 테케 10개 중 4개 맞음

import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    # V : 노드 개수, E : 간선 개수
    V, E = map(int, input().split())
    # 노드 개수만큼 인접 리스트 생성
    # 0번부터 V번까지 (0번은 없는 노드)
    adj = [[] for _ in range(V+1)]

    for _ in range(E):
        # 간선정보
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    # 출발노드, 도착노드
    S, G = map(int, input().split())

    # 깊이 탐색
    stack = [S]
    visited = [S]
    # 도착 지점까지 갈 수 있는 경로를 저장
    route = [S]
    cnt = 0

    # 현재 위치 v
    v = S
    while True:
        if v == G:
            break
        if v not in route:
            route.append(v)
            cnt += 1
        # v의 간선 중 갈 수 있는 노드가 있는지 확인
        for w in adj[v]:
            if w not in visited:
                v = w
                visited.append(v)
                stack.append(v)
                route.append(v)
                cnt += 1
                break
        # v의 인접 노드 중 갈 수 있는 곳이 없다면 스택 주워서 되돌아감
        else:
            if stack:
                v = stack.pop()
                route.pop()
                cnt -= 1
            else:
                break
    print('#{}' .format(tc), cnt)

