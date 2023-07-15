function solution(k, d) {
    // b <= (d ** 2 - (k * a) ** 2) ** 0.5 / k
    // y <= sqrt( d^2 - x^2)
    
    let answer = 0;
    for (let i = 0; i <= d; i += k) {
        const y = Math.floor((d ** 2 - i ** 2) ** 0.5 / k) + 1;
        answer += y;
    }
    return answer
}