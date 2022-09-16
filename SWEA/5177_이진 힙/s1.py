# SWEA 5177 이진 힙
# 220915

import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = [0] + list(map(int, input().split()))

    # 인덱스 = 노드번호
    tree = [0]

    for i in range(1, N+1):
        tree.append(nums[i])
        p = i // 2
        
        while tree[p] > tree[i]:
            tree[p], tree[i] = tree[i], tree[p]
            i = p
            p //= 2

    result = 0
    # 조상노드가 있을동안 진행
    while N:
        N //= 2
        result += tree[N]
    print('#{}' .format(tc), result)