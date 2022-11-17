function solution(num) {
    let cnt = 0;
    while (num !== 1 && cnt < 500)  {
        cnt ++;
        if (num % 2 === 0) {
            num /= 2
        } else {
            num = num * 3 + 1
        }
    }
    if (cnt < 500) return cnt;
    return -1;
}