function solution(a, b) {
    const length = a.length;
    let answer = 0;
    for (let i = 0; i < length; i++) {
        answer += a[i] * b[i]
    }
    return answer;
}