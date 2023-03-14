function solution(n){
    let cnt = 0;
    let total = n;
    
    while (total > 0) {
        // 홀수라면
        if (total % 2) {
            total--;
            cnt++;
        }
        // 짝수라면
        else {
            total /= 2
        }
    }
    return cnt
}