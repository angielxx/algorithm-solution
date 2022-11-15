function solution(s) {
    let answer = '';
    let flag = true;
    if (s[0] === '-') {
        flag = false;
        s = s.substring(1)
    }
    if (flag) {
        return Number(s)
    } else {
        return -(Number(s))
    }
    
}