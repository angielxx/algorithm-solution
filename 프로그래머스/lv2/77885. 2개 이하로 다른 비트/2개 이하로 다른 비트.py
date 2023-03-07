def solution(numbers):
    # 0111 - 1011
    # 01111 - 10111
    # 0이 있으면 제일 작은 자릿수 0을 1로 1바꿈
    # 0이 없으면 앞에 0하나 붙이고 앞의 큰 두자리를 반전
    answer = []
    
    for number in numbers:
        bin_number = list('0' + bin(number)[2:])
        idx = ''.join(bin_number).rfind('0')
        bin_number[idx] = '1'
        
        if number % 2:
            bin_number[idx + 1] = '0'
        
        answer.append(int(''.join(bin_number), 2))
            
    return answer