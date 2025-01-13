T = int(input())

for t in range(T):
    n = input()
    arr1 = list(map(int, input().split()))
    arr1.sort()
    
    m = input()
    arr2 = list(map(int, input().split()))

    answer = list()

    for t in arr2:
        s = 0
        e = len(arr1) - 1
        found = False
        
        while s <= e:
            m = (s + e) // 2
            if arr1[m] < t:
                s = m + 1
            elif arr1[m] > t:
                e = m - 1
            else:
                answer.append(1)
                found = True
                break;
        
        if not found:
            answer.append(0)
            
    for a in answer:
        print(a)
            