N = int(input())
"""
오답 ! 이차원 리스트 -> 얕은 복사됨
"""
arr = list()
for i in range(N):
    arr.append(['*'] * N)

def count(N):
    k = 0
    while True:
        if N == 1:
            break
        else:
            N /= 3
            k += 1
    return k
k = count(N)

# 반복에 사용될 3의 거듭제곱 숫자들
numbers = [3**i for i in range(k)]
# 바꿀 행과 열의 정보를 저장
to_change = list()

"""
1부터 1 4 7 10 13 16 19 22 25 = 1 + 3*n : 3*1증가 (1개)  1 + 3**1 * j
3부터 3 4 5, 12 13 14, 21 22 24 : 3*2씩 증가 (3개)   3 + 3**2 * j + j
9부터 10 11 12 13 14 15 16 17 18 : 3*3개   9 + 3**3 * j
N = 3 ** k
27 = 3 ** 3
"""
for i in numbers: # 1, 3, 9
    idx = numbers.index(i)
    index_list = list()
    
    for j in range(i): # 0  # 0,1,2 
        k = 0
        while i + (3 ** (idx + 1) * k) < N:
            index_list.append(i + (3 ** (idx + 1) * k) + j) 
            k += 1
    to_change.append(index_list)

for idx_list in to_change: # [1, 4, 7, 10, 13, 16, 19, 22, 25]
    for i in idx_list:
        for j in idx_list:
            arr[i][j] = ' '
                
for i in range(N):
    print(''.join(arr[i]), end='\n')