k, n = map(int, input().split(' '))

lines = []
max_line = 0

for _ in range(k):
    line = int(input())
    lines.append(line)
    
    if max_line < line:
        max_line = line
        
s = 1
e = max_line

answer = 1

while s <= e:
    m = (s + e) // 2
    
    total = 0
    
    for l in lines:
        total += l // m

    if total >= n:
        s = m + 1
    elif total < n:
        e = m - 1
        
print(e)