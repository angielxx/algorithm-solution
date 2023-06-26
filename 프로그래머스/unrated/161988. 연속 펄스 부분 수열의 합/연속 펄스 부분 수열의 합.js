function solution(seq) {
    const flag1 = Array.from({length:seq.length}, (v, idx) => {
        if (idx % 2) return -1
        else return 1
    })
    const flag2 = Array.from({length:seq.length}, (v, idx) => {
        if (idx % 2) return 1
        else return -1
    })
    
    let sum1 = 0;
    let sum2 = 0;
    let min1 = Infinity;
    let min2 = Infinity;
    let answer = 0;
    for (let i = 0; i < seq.length; i++) {
        min1 = Math.min(min1, sum1);
        min2 = Math.min(min2, sum2);
        sum1 += flag1[i] * seq[i];
        sum2 += flag2[i] * seq[i];
        answer = Math.max(sum1 - min1, sum2 - min2, answer);
    }
    return answer
}