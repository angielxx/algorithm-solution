def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    
    def dfs(start):
        visited[start] = True
        for i in range(n):
            if i != start and computers[start][i] and not visited[i]:
                dfs(i)
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
    return answer

