def solution(new_id):
    # 과정을 거쳐야하는지 체크하는 함수
    def isOk(S):
        status = False
        for i in range(len(S)):
            s = S[i]
            # 1단계
            if s.isupper():
                status = True
            # 2단계
            if s.isalnum() == False and s not in ['-', '_', '.']:
                status = True
            # 3단계
            if i+1 < len(S) and S[i] == '.' and S[i+1] == '.':
                status = True
        # 4단계
        if S[0] == '.' or S[-1] == '.':
            status = True
        # 5단계
        if not S:
            status = True
        # 6단계
        if len(S) >= 16:
            status = True
        # 7단계
        if len(S) <= 2:
            status = True
        return status 

    while isOk(new_id):
        step1 = new_id.lower()
        # print('1 :', step1)

        # 2단계
        step2 = ''
        for i in range(len(step1)):
            if step1[i].isalnum() or step1[i] in ['-', '_', '.']:
                step2 += step1[i]

        # print('2 :', step2)

        # 3단계
        step3 = ''
        stack = []
        for i in range(len(step2)):
            if step2[i] == '.':
                stack.append(step2[i])
            else:
                if stack:
                    step3 += '.'
                    stack.clear()
                step3 += step2[i]
        else:
            if stack:
                step3 += '.'

        # print('3 :', step3)

        # 4단계
        step4 = ''
        s, e = 0, len(step3)
        if step3[0] == '.':
            s = 1
        if step3[-1] == '.':
            e = len(step3) - 1
        step4 = step3[s:e]
        # print('4 :', step4)

        # 5단계
        if not step4:
            step4 = 'a'
        step5 = step4

        # 6단계
        step6 = step5[:15]

        # print('6 :', step6)

        # 7단계
        if len(step6) <= 2:
            step6 += step6[-1] * (3 - len(step6))
        step7 = step6

        # print('7 :', step7)

        new_id = step7

    return new_id