import collections
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        .most_common() : 최대 빈도를 내림차순으로 하여 (해당요소, 빈도수)가
        저장된 배열을 반환
        -> 인자가 없으면 전체 요소 출력
        -> 인자가 있으면 인자 요소만큼 상위 요소 출력
        """
        """
        .subtrack() : 각 요소의 값을 각각 빼준다. (값이 마이너스가 될 수 있음)

        example.
        task가 A일 때
        Counter({'A': 3, 'B': 3, 'C': 3, 'D': 2, 'E': 1})
        >> Counter({'B': 3, 'C': 3, 'A': 2, 'D': 2, 'E': 1})
        A가 3에서 2로 감소
        """

        counter = collections.Counter(tasks)
        # counter : Counter({'A': 3, 'B': 3, 'C': 3, 'D': 2, 'E': 1})

        # schedule 임시 추가
        schedule = []
        result = 0
        while True:
            print()
            print()
            print()
            print('start!')
            print()
            sub_count = 0

            # 개수 순 추출
            # n + 1을 추출했을 때 n+1개가 모두 나온다면, idle없이 계속 진행
            for task, _ in counter.most_common(n+1):
                print('most_common : ', counter.most_common(n+1))
                print('task', task)
                # sub_count ?
                sub_count += 1
                result += 1

                counter.subtract(task)
                schedule.append(task)

                print('schedule : ', schedule)
                # 0 이하인 아이템을 목록에서 완전히 제거
                # 빈 collections.Counter()를 더하는 것
                counter += collections.Counter()
                print('result in :', result)
                print()

            if not counter:
                break

            result += n - sub_count + 1
            print('result out :', result)

        return result

# tasks = ["A","A","A","B","B","B", "C","C","C", "D", "D", "E"]
# n = 2

tasks = ["A","A","A","B","B","B"]
n = 2

s = Solution()
print(s.leastInterval(tasks, n))