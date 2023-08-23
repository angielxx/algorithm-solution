import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

# 각 위치에 최소로 도달할 수 있는 시간을 저장
visited = [sys.maxsize] * 100001
q = deque([(n, 0)]) # 위치, 시간
visited[n] = 0

while q:
    now, time = q.popleft()
    
    if now == k:
        break
    
    # 걷는 경우
    if now - 1 >= 0:
        if visited[now - 1] > time + 1:
            visited[now - 1] = min(visited[now - 1], time + 1) # 큐에 같은 위치가 중복해서 들어가는 경우를 방지하기 위함
            q.append((now - 1, time + 1))
            
    if now + 1 <= 100000:
        if visited[now + 1] > time + 1:
            visited[now + 1] = min(visited[now + 1], time + 1)
            q.append((now + 1, time + 1))
    # 순간이동
    if now * 2 <= 100000:
        if visited[now * 2] > time:
            visited[now * 2] = min(visited[now * 2], time)
            q.append((now * 2, time))   

print(visited[k])