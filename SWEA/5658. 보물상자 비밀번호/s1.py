# 5658. 보물상자 비밀번호
# 220826

import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    hexa = list(input())

    # 한 변에 들어가는 숫자의 개수 3
    n = N // 4

    # 모든 숫자 넣는 리스트
    nums = []

    # 회전 시키기 : 0회 ~ 2회
    for i in range(n):
        if i == 0:
            pass
        else:
            last = hexa.pop()
            hexa = [last] + hexa
        # print(hexa)
        for j in range(N//n): # 012
            num = ''
            for k in range(n): # 012
                num += hexa[n*j+k] # [0:3] [3:6] [6:9] [9:12]
            nums.append(num)

    # 중복 숫자 제거
    nums = list(set(nums))

    # len 함수 구현
    length = 0
    for num in nums:
        length += 1

    # 정렬하기 : bubble sort
    for i in range(length-1):
        for j in range(i+1, length):
            # print(i, j)
            if int(nums[i], 16) < int(nums[j], 16):
                nums[i], nums[j] = nums[j], nums[i]
    # K번째 숫자 출력
    print('#{}' .format(tc),int(nums[K-1], 16))