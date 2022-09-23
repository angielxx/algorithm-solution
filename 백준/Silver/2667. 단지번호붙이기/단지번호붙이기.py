# 지도의 크기
N = int(input())

# N개의 자료
arr = [input() for _ in range(N)]

# 방문 배열, 델타 세팅
visited = [[False] * N for _ in range(N)]
delta = [[1,0], [-1,0], [0,1], [0,-1]]

# 단지내의 집 수 리스트에 저장
cnt_list = []

total = 0
for i in range(N):
    for j in range(N):
        cnt = 0
        if arr[i][j] == '1' and visited[i][j] == False:
            total += 1
            stack = [(i, j)]
            visited[i][j] = True
            while stack:
                si, sj = stack.pop()
                visited[si][sj] = True
                cnt += 1
                for k in range(4):
                    ni, nj = si + delta[k][0], sj + delta[k][1]
                    if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == '1' and visited[ni][nj] == False:
                        if (ni, nj) not in stack:
                            stack.append((ni, nj))
            cnt_list.append(cnt)
            # print('done', cnt)
print(total)
cnt_list.sort()
for i in range(total):
    print(cnt_list[i])