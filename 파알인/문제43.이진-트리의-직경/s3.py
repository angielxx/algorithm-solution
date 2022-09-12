# 543. Diameter of Binary Tree
# 220912

# 풀이 참고 후 코드 구현

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    longest = 0
    
    def diameterOfBinaryTree(self, root):
        def dfs(root):
            if not root:
                return -1

            left = dfs(root.left)
            right = dfs(root.right)

            distance = left + right + 2
            self.longest = max(distance, self.longest)
            return max(left, right) + 1
        
        dfs(root)
        return self.longest

# root = TreeNode(val=1, left=TreeNode(val=2, left=None, right=None), right=None)
# root = TreeNode(val=4, left=TreeNode(val=2, left=TreeNode(3, TreeNode(5, None, None), right=TreeNode(1, None, None)), right=None), right=None)
root = TreeNode(val=1, left=TreeNode(val=2, left=TreeNode(val=4, left=None, right=None), right=TreeNode(val=5, left=None, right=None)), right=TreeNode(val=3, left=None, right=None))
s = Solution()
print(s.diameterOfBinaryTree(root))