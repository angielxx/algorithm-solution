def get_total(long, short):
    total_list = []
    for i in range(len(long) - len(short) + 1):
        total = 0
        for j in range(len(short)):
            total += long[i+j] * short[j]
        total_list.append(total)
    total_list.sort(reverse=True)
    return total_list[0]

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    if N > M:
        result = get_total(A, B)
    else:
        result = get_total(B, A)
    print(f'#{tc}', result)