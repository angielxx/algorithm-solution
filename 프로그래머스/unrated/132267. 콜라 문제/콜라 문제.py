def solution(a, b, n):
    cnt = 0
    while ( n >= a):
        rest = n % a
        n = (n // a) * b
        cnt += n
        n += rest
    return cnt