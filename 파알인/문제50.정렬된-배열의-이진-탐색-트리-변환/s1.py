# 108. Convert Sorted Array to Binary Search Tree
# 220912

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums):
        def getTree(nums):
            if not nums:
                return None
            mid = len(nums) // 2
            val = nums[mid]
            left = getTree(nums[:mid])
            right = getTree(nums[mid+1:])
            return TreeNode(val, left, right)
        
        tree = getTree(nums)
        return tree
        
nums = [-10,-3,0,5,9]
# nums = [1,3]

s = Solution()
print(s.sortedArrayToBST(nums))