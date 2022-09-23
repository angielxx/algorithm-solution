n = int(input())
switches = [0 for i in range(n)]
switches = list(map(int, input().split()))

stu_num = int(input())
for stu in range(stu_num) :
    gender, idx = map(int, input().split())
    if gender == 1 :
        change_idx = idx - 1
        while change_idx < n :
            if switches[change_idx] == 0 :
                switches[change_idx] = 1
            else :
                switches[change_idx] = 0
            change_idx += idx
    else :
        left_idx = right_idx = idx - 1
        while left_idx >= 0 and right_idx < n :
            if switches[left_idx] == switches[right_idx] :
                if switches[left_idx] == 0 :
                    switches[left_idx] = 1
                    switches[right_idx] = 1
                else :
                    switches[left_idx] = 0
                    switches[right_idx] = 0
                left_idx -= 1
                right_idx += 1
            else :
                break

for i in range(n) :
    print(switches[i], end = ' ')
    if (i + 1) % 20 == 0 :
        print()