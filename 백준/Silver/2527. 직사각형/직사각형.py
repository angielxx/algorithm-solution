def search(lst):
    ai1, aj1, ai2, aj2, bi1, bj1, bi2, bj2 = lst
    # d인 경우
    if (ai2 < bi1) or (ai1 > bi2) or (aj1 > bj2) or (aj2 < bj1):
        return 'd'

    # b와 c인 경우
    elif (ai1 == bi2) or (ai2 == bi1):
        if (aj2 == bj1) or (aj1 == bj2): return 'c'
        else: return 'b'

    elif (aj1 == bj2) or (aj2 == bj1):
        if (ai2 == bi1) or (ai1 == bi2): return 'c'
        else: return 'b'

    return 'a'

for _ in range(4):
    lst = list(map(int, input().split()))
    print(search(lst))