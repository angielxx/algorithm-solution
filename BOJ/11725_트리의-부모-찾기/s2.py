# BOJ 11275 트리의 부모 찾기
# 220914

import sys

# 노드의 개수
N = int(sys.stdin.readline())
# 입력값 받기
data = [list(map(int, sys.stdin.readline().split())) for _ in range(N-1)]

# 방문 처리
visited = [0] * (N+1)
# 자식을 인덱스로 부모 노드 저장
par = [0] * (N+1)

def bfs(root):
    