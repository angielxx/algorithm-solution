T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    binary = bin(M)[2:]
    binary = list(binary)

    status = 'ON'
    for _ in range(N):
        if not binary:
            status = 'OFF'
            break
        if binary and binary.pop() != '1':
            status = 'OFF'
            break
        
    print('#{}' .format(tc), status)