# SWEA 5176 이진탐색
# 220915

import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    
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

    # 각 노드의 값 저장
    # 인덱스가 노드번호 - 1
    arr = [0] * (N+1)

    # dfs로 값 넣기
    i = 1
    def inorder(n):
        global i
        if n:
            inorder(ch1[n])
            arr[n] = i
            i += 1
            inorder(ch2[n])
    inorder(1)
    print('#{}' .format(tc), arr[1], arr[N//2])