# BOJ 1003 피보나치 함수
# 220820

T = int(input())

for _ in range(T):
    N = int(input())

    zero_list = [1, 0]
    one_list = [0, 1]

    for i in range(2, N+1):
        zero = zero_list[i-1] + zero_list[i-2]
        one = one_list[i-1] + one_list[i-2]

        zero_list.append(zero)
        one_list.append(one)

    print(zero_list[N], one_list[N])