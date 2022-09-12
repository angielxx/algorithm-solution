# 543. Diameter of Binary Tree
# 220912

# 틀림
# 왼쪽의 최대 깊이와 오른쪽의 최대 깊이의 합을 구하는 로직

import collections
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        if root is None:
            return 0

        def getDepth(root):
            queue = collections.deque([root])
            depth = 0
            
            while queue:
                depth += 1
                for _ in range(len(queue)):
                    cur_root = queue.popleft()
                    if cur_root.left:
                        queue.append(cur_root.left)
                    if cur_root.right:
                        queue.append(cur_root.right)
            return depth

        result = 0
        if root.left:
            result += getDepth(root.left)
        if root.right:
            result += getDepth(root.right)
        return result

# root = TreeNode(val=1, left=TreeNode(val=2, left=None, right=None), right=None)
# root = TreeNode(val=4, left=TreeNode(val=2, left=TreeNode(3, TreeNode(5, None, None), right=TreeNode(1, None, None)), right=None), right=None)

root = TreeNode(val=1, left=TreeNode(val=2, left=TreeNode(val=4, left=None, right=None), right=TreeNode(val=5, left=None, right=None)), right=TreeNode(val=3, left=None, right=None))
s = Solution()
print(s.diameterOfBinaryTree(root))
