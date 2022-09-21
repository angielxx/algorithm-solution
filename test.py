def f(i, k):
    if i == k:
        print(bit)
    else:
        bit[i] = 0
        f(i+1, k)
        bit[i] = 1
        f(i+1, k)


arr = [3,6,7,1,5,4]
n = len(arr)

# bit[i] arr[i]가 부분집합의 원소인지 표시
bit = [0] * n
f(0, n)