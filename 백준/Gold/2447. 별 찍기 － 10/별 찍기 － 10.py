N = int(input())
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

numbers = [3**i for i in range(k)]
to_change = list()

for i in numbers:
    idx = numbers.index(i)
    index_list = list()
    
    for j in range(i):
        k = 0
        while i + (3 ** (idx + 1) * k) < N:
            index_list.append(i + (3 ** (idx + 1) * k) + j) 
            k += 1
    to_change.append(index_list)

for idx_list in to_change:
    for i in idx_list:
        for j in idx_list:
            arr[i][j] = ' '
                
for i in range(N):
    print(''.join(arr[i]), end='\n')