# SWEA 5178 노드의 합
# 220915

import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    # 노드의 개수, 리프 노드의 개수, 값을 출력할 노드 번호
    N, M, L = map(int, input().split())

    ch1 = [0] * (N+1)
    ch2 = [0] * (N+1)
    par = [0] * (N+1)

    # 완전 이진 트리 모양부터 잡기
    def makeTree(root):
        # left = root * 2
        # right = root * 2 + 1
        left = root * 2
        right = root * 2 + 1
        if left <= N:
            ch1[root] = left
            par[left] = root
            makeTree(left)
        if right <= N:
            ch2[root] = right
            par[right] = root
            makeTree(right)
    makeTree(1)

    # 각 노드의 값을 저장
    arr = [0] * (N+1)

    # 리프노드 정보 저장
    for _ in range(M):
        node, num = map(int, input().split())
        arr[node] = num

    # dfs로 리프노드부터 상태값 누적
    def dfs(root):
        global arr
        # 노드의 값이 0이 아니면 리프노드라는 뜻
        if arr[root]:
            return arr[root]
        else:
            result = 0
            # 왼쪽이 있으면
            if ch1[root]:
                result += dfs(ch1[root])
            # 오른쪽이 있으면
            if ch2[root]:
                result += dfs(ch2[root])
            return result
    print('#{}' .format(tc), dfs(L))