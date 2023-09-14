import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())

if n < 2:
    print(9)
else:
    next = {0: [1], 1: [2,0], 2: [3, 1], 3: [4, 2], 4: [5, 3], 5: [6, 4], 6: [7, 5], 7: [8, 6], 8: [9, 7], 9: [8]}
    
    dp = [0] * (n + 1)
    dp[1] = 9
    before = defaultdict(int)
    
    for i in range(1, 10):
        before[i] = 1
        
    for i in range(2, n + 1):
        now = defaultdict(int)
        total = 0
        for key, val in before.items():
            for num in next[key]:
                now[num] += val
                total += val
        dp[i] = total
        before = now

    print(dp[n] % 1000000000)