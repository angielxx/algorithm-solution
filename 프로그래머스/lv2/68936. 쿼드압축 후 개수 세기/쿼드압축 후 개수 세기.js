function solution(arr) {
    const answer = [0, 0];
    function quad(si, sj, ei, ej) {
        const mi = (si + ei) / 2;
        const mj = (sj + ej) / 2;
        
        let flag = true;
        for (let i = si; i < ei; i++) {
            for (let j = sj; j < ej; j++) {
                if (arr[si][sj] !== arr[i][j]) {
                    flag = false;
                    break;
                }
            }
        }
        if (flag) {
            if (arr[si][sj]) answer[1]++;
            else answer[0]++;
            return
        }
        quad(si, sj, mi, mj);
        quad(si, mj, mi, ej);
        quad(mi, sj, ei, mj);
        quad(mi, mj, ei, ej);
    }
    
    quad(0, 0, arr.length, arr.length);
    return answer
}