# SWEA 5099. 피자 굽기
# 220825

import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    # 화덕의 크기, 피자 개수
    N, M = map(int, input().split())
    # M개의 피자에 뿌려진 치즈 양
    pizza = list(map(int, input().split()))

    # 리스트의 값들을 (피자번호, 치즈양)으로 바꾸기
    for i, n in enumerate(pizza):
        pizza[i] = [i+1, n]

    # 화덕의 크기만큼 화덕에 피자 넣기
    fire = []
    for i in range(N):
        fire.append(pizza.pop(0))

    # 피자를 체크, while문이 끝나면 맨 마지막에 남아있던 피자가 저장
    check = []
    while fire:
        # print(fire, pizza)
        # 화덕 맨 앞의 피자 확인 (피자번호, 치즈양)
        check = fire.pop(0)
        cheese = check[1] // 2
        # 바뀐 치즈 양으로 값 변경
        check[1] = cheese
        # 치즈양 확인
        if cheese == 0:
            # 남아있는 피자가 있으면 화덕에 넣기
            if pizza:
                fire.append(pizza.pop(0))
            # 남아있는 피자가 없으면 그대로 진행
            else:
                pass
        else:
            fire.append(check)
    print('#{}' .format(tc), check[0])
