# 104. Maximum Depth of Binary Tree
# 220912

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    
    def maxDepth(self, root):
        max_route = []
        
        def dfs(root, route):
            # 리트코드에 넣으니 nonlocal이 systax error로 뜸
            # 클래스 변수로 넣으니 작동
            nonlocal max_route

            if not root:
                return

            if root.left != None:
                dfs(root.left, route + [root.val])
            if root.right != None:
                dfs(root.right, route + [root.val])
            if root.left == None and root.right == None:
                route += [root.val]
                if len(route) > len(max_route):
                    max_route = route
                    return
        
        dfs(root, [])
        return len(max_route)

root = TreeNode(val=3, left=TreeNode(val=9, left=None, right=None), right=TreeNode(val=20, left=TreeNode(val=15, left=None, right=None), right=TreeNode(val=7, left=None, right=None)))

s = Solution()
print(s.maxDepth(root))