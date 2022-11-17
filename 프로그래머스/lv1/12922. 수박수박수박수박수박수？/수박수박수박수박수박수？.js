function solution(n) {
    let answer = '';
    const repeat = Math.floor(n/2)
    for (let i = 0; i < repeat; i++) {
        answer += '수박'
    }
    if (n % 2) {
        answer += '수'
    }
    return answer
}