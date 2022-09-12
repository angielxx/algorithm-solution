import collections
import queue


class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0
        queue = collections.deque([root])
        depth = 0

        while queue:
            depth += 1
            # 큐 연산 추출 노드의 자식 노드 삽입
            for _ in range(len(queue)):
                cur_root = queue.popleft()
                if cur_root.left:
                    queue.append(cur_root.left)
                if cur_root.right:
                    queue.append(cur_root.right)
        return depth

"""
<Result>
Runtime: 52 ms, faster than 26.21% of Python online submissions for Maximum Depth of Binary Tree.
Memory Usage: 15.9 MB, less than 88.24% of Python online submissions for Maximum Depth of Binary Tree.
"""