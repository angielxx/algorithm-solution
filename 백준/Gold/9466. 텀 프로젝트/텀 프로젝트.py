# 2023.8.19
# 78%에서 시간초과

import sys
input = sys.stdin.readline

t = int(input())

def dfs(start):
    stack = [(start, [start])]
    
    while stack:
        now, route = stack.pop()

for _ in range(t):
    n = int(input())
    arr = [0] + list(map(int, input().strip().split(' ')))
    
    answer = 0
    visited = [0 for _ in range(n+1)]
    
    for i in range(1, n+1):
        if visited[i]: continue
        
        route = []
        stack = [i]
        while stack:
            now = stack.pop()
            visited[now] = 1
            route.append(now)
            
            # 다음 팀원이 이미 방문한 경우, 경로에 있는 경우, 싸이클이 만들어지는 경우임
            if visited[arr[now]]:
                # 경로 중간이면, 중간 그 전은 모두 팀에 속할 수 없음
                if arr[now] in route:
                    answer += route.index(arr[now])
                else:
                    answer += len(route)
            # 다음으로 갈 수 있는 경우
            else:
                stack.append(arr[now])
    print(answer)