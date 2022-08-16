T = int(input())

for t in range(T):
    cases = []
    string = str()
    print(f'#{t+1}')
    N = int(input())
    cases = list(input() for _ in range(N))
    for case in cases:
        C, K = case.split()
        string += C * int(K)
    length = len(string)
    row = length // 10 + 1
    for r in range(row):
        print(string[10*r : 10*(r+1)])
