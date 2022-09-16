# SWEA 1232 사칙연산
# 220915

import sys
sys.stdin = open('input.txt', 'r')

T = 10

# len 구현
def len(iterable):
    length = 0
    for n in iterable:
        length += 1
    return length

for tc in range(1, T+1):
    # 정점의 개수
    N = int(input())

    # 정점번호를 인덱스로, 각 값을 저장
    arr = [0]* (N+1)

    # 부모 번호를 인덱스로, 자식 번호를 저장
    ch1 = [-1] * (N+1)
    ch2 = [-1] * (N+1)

    # 입력값 저장
    for _ in range(N):
        info = list(input().split())
        node = int(info.pop(0))
        val = info.pop(0)
        # 숫자면 리프트리
        if val.isnumeric():
            arr[node] = val
        # 숫자가 아니면 연산자라는 뜻이며, 자식노드가 있음
        else:
            arr[node] = val
            p = node
            c1 = int(info.pop(0))
            c2 = int(info.pop(0))
            ch1[p], ch2[p] = c1, c2

    # 계산기
    def cal(opt, num1, num2):
        if opt == '+':
            return num1 + num2
        elif opt == '-':
            return num1 - num2
        elif opt == '*':
            return num1 * num2
        elif opt == '/':
            return num1 / num2

    # 자신의 상태값을 연산값으로 bfs 누적
    def dfs(n):
        # 숫자면 자신의 값을 상태값으로 리턴
        if arr[n].isnumeric():
            return int(arr[n])
        # 연산자면 연산값을 상태값으로 리턴
        else:
            left = dfs(ch1[n])
            right = dfs(ch2[n])
            return int(cal(arr[n], left, right))
    
    print('#{}' .format(tc), dfs(1))