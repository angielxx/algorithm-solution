# 42. Trapping Rain Water
# 220820

# Time Limit Exceeded

class Solution(object):
    def trap(self, height):
        N = len(height)

        s, e = 0, 0
        h1, h2 = 0, 0
        # 시작지점 찾기
        for i in range(N):
            if height[i] > 0:
                s = i
                h1 = height[i]
                break

        # 탐색 시작
        rain = 0
        while s < N-1:
            # 다음 높은 기둥 찾기
            next = False
            for i in range(s+1, N):
                if height[i] > h1:
                    h2 = height[i]
                    e = i
                    next = True
                    break
            # 다음 높은 기둥이 있으면
            if next:
                for i in range(s+1, e):
                    rain += (h1 - height[i])
                h1 = h2
            # 다음 높은 기둥이 없으면
            # 뒤의 영역에서 가장 높은 기둥 찾기
            else:
                # h2 찾기
                h2 = 0
                next2 = False
                for i in range(s+1, N):
                    if height[i] > h2:
                        h2 = height[i]
                        e = i
                        next2 = True
                # 빗물 계산
                if next2:
                    for i in range(s+1, e):
                        rain += (h2 - height[i])
                else:
                    break
                h1 = h2
            s = e
        return rain

height = [0,2,0]
s = Solution()
print(s.trap(height))