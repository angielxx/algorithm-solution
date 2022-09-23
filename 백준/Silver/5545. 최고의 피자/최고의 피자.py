# 토핑의 종류의 수
N = int(input())
# 도우의 가격, 토핑의 가격
A, B = map(int, input().split())
# 도우의 열량
C = int(input())
# N개의 토핑의 열량
toppings = [int(input()) for _ in range(N)]

# i번째까지의 합이 i+1 ~ N-1 까지의 합보다 클 때
# 제일 토핑의 수를 적게 선택하면서, 토핑의 열량을 가장 높게 가져갈 수 있음 (가격은 모두 동일하기 때문에)
# 0개 선택부터 토핑의 수를 열량이 큰 것부터 하나씩 선택해가며 1원당 열량을 구한다.
# 높아지다가 작아지는 값이 나왔을 때 정답을 출력한다.
toppings.sort(reverse=True)

# 토핑 열량의 합
sum_tops = 0
cnt = 0
# 칼로리 총합
cal = C
# 가격
price = A
# 1원당 열량
result = cal / price
# 스택에 1원당 열량 순서대로 저장, 값이 작아질 때 마지막 원소 출력
answer = result
for i in range(N):
    cal += toppings[i]
    price += B
    result = cal / price
    if result > answer:
        answer = result
    else:
        break

print(int(answer))