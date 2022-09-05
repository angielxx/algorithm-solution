# 39. Combination Sum
# 220905

"""
로직
1. 예외 처리 : sum(candidates) > target ? []
2. 
"""

class Solution(object):
    def combinationSum(self, candidates, target):
        combi = []
        # comsum : 지금까지 조합의 총합
        # idx
        def dfs(comsum, idx, path):
            if comsum == target:
                combi.append(path)
                return path
            elif comsum > target:
                return
            # 아직 합이 target보다 작을 때
            else:
                for i in range(idx, len(candidates)):
                    dfs(comsum + candidates[i], i, path + [candidates[i]])

        path = []
        dfs(0, 0, path)
        return combi

candidates = [2,3,6,7]
target = 7

s = Solution()
print(s.combinationSum(candidates, target))