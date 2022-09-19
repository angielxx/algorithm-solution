# Leetcode 621. Task Scheduler
# 220919

class Solution(object):
    def leastInterval(self, tasks, n):
        
        # stack = [0] * (10**4)
        stack = [0] * (105)
        for i in range(len(tasks)):
            # 현재 스케줄링 하려고 하는 태스크
            task = tasks[i]

            j = 0
            while j < len(stack):
                # idle이면(빈칸이면) 조건 확인
                if stack[j] == 0:
                    status = True
                    # 앞 뒤로 n조건 만족하는지 확인
                    for k in range(1, n+1):
                        if not status:
                            break
                        check_front = j - k
                        check_back = j + k
                        if 0 <= check_front < len(stack):
                            if stack[check_front] == task:
                                status = False
                        if 0 <= check_back < len(stack):
                            if stack[check_back] == task:
                                status = False

                    # j번째에 배치할 수 있는 경우
                    if status:
                        stack[j] = task
                        break
                    # j번째에 배치할 수 없는 경우
                    else:
                        j += 1
                # idle이 아니라면 다음 칸 보기    
                else:
                    j += 1
        print(stack)
        cnt = 0
        for i in range(len(stack)):
            if stack[i:] == [0] * (len(stack) - i):
                cnt = i
                break
            else:
                pass
        return cnt
        
# tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
# n = 2

# tasks = ["A","A","A","B","B","B"]
# n = 50

tasks = ["A","A","A","B","B","B", "C","C","C", "D", "D", "E"]
n = 2

s = Solution()
print(s.leastInterval(tasks, n))