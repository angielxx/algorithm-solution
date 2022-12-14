import sys
input = sys.stdin.readline

bracket = input().strip()
stack = []
temp = 0
flag = True

pair = {
    ')' : '(',
    ']' : '['
}

for s in bracket:
    # print(stack)
    # print(flag)
    # print(s)
    if s == '(' or s == '[':
        stack.append(s)
    else:
        if stack and isinstance(stack[-1], int):
            while stack and isinstance(stack[-1], int):
                temp += stack.pop()
        if not stack:
            flag = False
            break
        if stack.pop() == pair[s]:
            value = 2 if pair[s] == '(' else 3
            if temp == 0:
                stack.append(value)
            else:
                stack.append(temp * value)
                temp = 0
        else:
            flag = False
            break
# print('here', flag)
answer = 0
for s in stack:
    if isinstance(s, int):
        answer += s
    else:
        flag = False
        break
if flag:
    print(answer)
if not flag:
    print(0)