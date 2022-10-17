# BOJ 4256 트리
# 221017

import sys
input = sys.stdin.readline

def getTree(preorder, inorder):
    if len(preorder) == 1:
        return preorder[0]
    if not preorder:
        return

    root = preorder[0]
    root_idx = inorder.index(root)

    left_inorder = inorder[:root_idx]
    right_inorder = inorder[root_idx + 1:]

    left_preorder = preorder[1 : 1 + len(left_inorder)]
    right_preorder = preorder[1 + len(left_inorder) : ]

    left_root = getTree(left_preorder, left_inorder)
    right_root = getTree(right_preorder, right_inorder)

    if left_root:
        ch1[root] = left_root
    if right_root:
        ch2[root] = right_root
    return root

def postorder(root):
    global post
    if ch1[root]:
        postorder(ch1[root])
    if ch2[root]:
        postorder(ch2[root])
    post.append(root)

T = int(input())
for _ in range(T):
    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))

    ch1 = [0] * (n+1)
    ch2 = [0] * (n+1)
    p = [0] * (n+1)
    root = preorder[0]

    getTree(preorder, inorder)

    post = []
    postorder(root)
    print(*post)