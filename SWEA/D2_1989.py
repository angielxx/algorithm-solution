num = int(input())
cases = list(input() for _ in range(num))

is_palindrome = True
def isPalindrome(string): # level [ l e v e l ]
    """
    global 넣어주기 전에
    UnboundLocalError:
    local variable 'is_palindrome' referenced before assignment
    """
    length = len(string) # length = 5
    for n in range(length // 2 - 1): # [ 0, 1 ]
        global is_palindrome
        if string[n] != string[length-(n+1)]: # 0 & 4 / 1 & 3
            is_palindrome = False
            break
    return is_palindrome

"""
True를 출력해야 할 때
<built-in function globals>
가 출력됌
오답 : is_palindrome = globals
"""

for case in cases:
    idx = cases.index(case)
    is_palindrome = True
    isPalindrome(case)
    if is_palindrome == True:
        print(f'#{idx+1} 1')
    else:
        print(f'#{idx+1} 0')