# SWEA 1238 contact
# 220914

import sys
sys.stdin = open('input.txt', 'r')

T = 10

# len 구현
def len(iterable):
    length = 0
    for i in iterable:
        length += 1
    return length

# 테케 시작
for tc in range(1, T+1):
    # 데이터 길이, 시작점 번호
    N, S = map(int, input().split())

    # 데이터
    data = list(map(int, input().split()))

    # 인접리스트
    # 부모를 인덱스로 자식 번호 리스트로 저장
    adj = [ [] for _ in range(101)]
    for i in range(N//2):
        p, c = data[i*2], data[i*2+1]
        # {from, to}쌍이 반복되는 경우 처리
        if c not in adj[p]:
            adj[p].append(c)

    # 방문하면 저장
    visited = []
    check_depth = []

    # 최대 깊이, 연락한 번호
    max_depth = 0
    max_num = 0

    # 깊이
    depth = 0

    # bfs
    def bfs(S):
        global depth
        global max_depth
        global max_num
        queue = [S]

        while queue:
            depth += 1
            for _ in range(len(queue)):
                v = queue.pop(0)
                if v not in visited:
                    visited.append(v)

                    # 자식 노드 확인해서 큐에 넣기
                    ch = adj[v]
                    # 갈 수 있는 자식만 넣기
                    okay = []
                    for c in ch:
                        if c not in visited:
                            okay.append(c)
                    # 연락할 곳이 있는 경우
                    if okay:
                        queue += okay
                    # 더 이상 연락할 곳이 없는 경우
                    else:
                        check_depth.append((v, depth))
                        # 깊이가 더 깊으면
                        if depth > max_depth:
                            max_depth = depth
                            max_num = v
                        # 깊이가 같으면 큰 번호로 비교
                        elif depth == max_depth:
                            if v > max_num:
                                max_num = v
                        
    bfs(S)
    print('#{}' .format(tc), max_num)

