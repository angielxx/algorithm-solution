function solution(scores) {
    const wan = scores[0];
    
    const wans_score = wan[0] + wan[1];
    
    scores.sort((a, b) => {
        const t = b[0] - a[0];
        if (t) return t
        else return a[1] - b[1];
    });
    
    let answer = 1;
    let x = 0;
    
    for (let score of scores) {
        if (wan[0] < score[0] && wan[1] < score[1]) return -1;
        
        if(wans_score < score[0] + score[1] && x <= score[1]) {
            answer++;
            x = score[1]
        }
    }
    return answer
}