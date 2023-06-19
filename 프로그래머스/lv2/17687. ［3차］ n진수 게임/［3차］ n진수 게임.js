function solution(n, t, m, p) {
    // p : 숫자를 m으로 나눈 나머지가 p
    // 말해야하는 숫자 : m * i + p (i = 0, 1,2,3... < t)

    let string = '';
    let num = 0;
    while (string.length < t * m) {
        string += num.toString(n);
        num++;
    }
    let answer = '';
    for (let i = 0; i < t; i++) {
        const idx = m * i + p - 1;
        answer += string[idx]
    }

    return answer.toUpperCase()
}