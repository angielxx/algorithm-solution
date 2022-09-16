# SWEA 5714 subtree
# 220915

import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    # 간선 수, 노드 N(을 루트로 하는 서브트리)
    E, N = map(int, input().split())

    # 트리 정보
    arr = list(map(int, input().split()))
    
    # 부모 노드를 인덱스로, 자식 노드를 저장
    ch1 = [0] * (E+2)
    ch2 = [0] * (E+2)

    # arr 길이 = 간선 수 * 2
    for i in range(E):
        p, c = arr[i*2], arr[i*2+1]
        # 왼쪽 자식 저장 안 되어 있으면 ch1에 저장
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c

    # 자신의 상태값 = 왼쪽 자식의 상태값 + 오른쪽 자식의 상태값
    cnt = 0
    def dfs(n):
        global cnt
        cnt += 1
        # 왼쪽 자식이 있으면
        if ch1[n]:
            dfs(ch1[n])
        # 오른쪽 자식이 있으면
        if ch2[n]:
            dfs(ch2[n])

    dfs(N)
    print('#{}' .format(tc), cnt)