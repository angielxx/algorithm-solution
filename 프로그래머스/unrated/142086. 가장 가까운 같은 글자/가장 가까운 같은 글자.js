function solution(s) {
    const answer = Array(s.length).fill(0);
    for (let i = 0; i < s.length; i++) {
        const me = s[i];
        let flag = false;
        for (let j = i - 1; j >=0; j--) {
            if (s[j] === me) {
                answer[i] = i - j;
                flag = true;
                break;
            }
        }
        if (!flag) answer[i] = -1;
    }
    return answer
}