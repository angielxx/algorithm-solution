class Solution(object):
    def combinationSum(self, candidates, target):
        result = []
        
        # csum : 합을 갱신
        # index : 자기자신을 포함하는 순서
        # path : 지금까지의 탐색 경로
        def dfs(csum, index, path):
            # 종료조건
            if csum < 0:
                return
            if csum == 0:
                result.append(path)
                return

            # 자신부터 하위 원소까지의 나열 재귀 호출
            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], i, path + candidates[i])

        dfs(target, 0, [])
        return result