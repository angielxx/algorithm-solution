# 연습문제2 부분집합
# 220822

A = [1,2,3,4,5,6,7,8,9,10]

def f(i, N, s, t):
    global result
    if i == N:
        total = 0
        temp = []
        for i in range(N):
            if bit[i]:
                total += A[i]
                temp.append(A[i])
        if total == 10:
            result.append(temp)
    else:
        # i번째 원소가 포함되지 않는 경우
        bit[i] = 0
        f(i+1, 10, s, t)
        # i번째 원소가 포함되는 경우
        bit[i] = 1
        f(i+1, 10, s, t)
    return result

result = []
bit = [0] * 10
s = 0
print(f(0, 10, 0, 10))