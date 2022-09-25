
T = 10

for _ in range(1, T+1):
    tc, N = map(int, input().split())
    line = list(map(int, input().split()))
    graph = [ [] for _ in range(100)]

    for i in range(N):
        a, b = line[2*i], line[2*i+1]
        graph[a].append(b)

    # 방문한 정점
    visited = [0]
    # 되돌아갈 정점
    stack = [0]

    result = 0
    v = 0
    while result == 0:
        for w in graph[v]:
            # 방문할 정점이 있으면 전진
            if w not in visited:
                if w == 99:
                    result = 1
                    break
                stack.append(w)
                v = w
                visited.append(v)
                break
        else:
            if stack:
                # 방문할 정점이 없을 때 빵가루 주워서 되돌아가기
                v = stack.pop()
            else:
                break

    print('#{} {}' .format(tc, result))