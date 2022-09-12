# 1038. Binary Search Tree to Greater Sum Tree
# 220912

# Definition for a binary tree node.
import collections

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def bstToGst(self, root):
        
        def rightSum(root):
            s = 0
            queue = collections.deque([root.right])
            while queue:
                cur_root = queue.popleft()
                if cur_root:
                    s += cur_root.val
                    if cur_root.left:
                        queue.append(cur_root.left)
                    if cur_root.right:
                        queue.append(cur_root.right)
            return s
        
        def getGst(root, parent=0):
            if root:
                val = parent + root.val + rightSum(root)
                left = getGst(root.left, val)
                right = getGst(root.right, parent)
                return TreeNode(val, left, right)

        return getGst(root)
        
            
root = TreeNode(val=4, left=TreeNode(val=1, left=TreeNode(val=0, left=None, right=None), right=TreeNode(val=2, left=None, right=TreeNode(val=3, left=None, right=None))), right=TreeNode(val=6, left=TreeNode(val=5, left=None, right=None), right=TreeNode(val=7, left=None, right=TreeNode(val=8, left=None, right=None))))
s = Solution()
print(s.bstToGst(root))