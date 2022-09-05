# 77. Combinations
# 220905

class Solution(object):
    def combine(self, n, k):
        nums = [i for i in range(1, n+1)]
        results = []
        def dfs(idx, path):
            if len(path) == k:
                results.append(path)
            else:
                for i in range(idx+1, n):
                    if nums[i] not in path:
                        dfs(i, path + [nums[i]])

        dfs(-1, [])
        return results

        
n = 4
k = 2
s = Solution()
print(s.combine(n, k))