function solution(places) {
    const answer = [];
    
    for (const place of places) {
        let flag = true;
        for (let i = 0; i < 5; i++) {
            if (!flag) break;
            for (let j = 0; j < 5; j++) {
                if (place[i][j] == 'P') {
                    if (!check(i, j, place)) {
                        flag = false;
                        break;
                    }
                }
            }
        }
        answer.push(Number(flag))
    }
    return answer
}

function check(i, j, board) {
    let answer = true;
    
    // 상하좌우로 cnt 2까지
    const di = [-1, 1, 0, 0];
    const dj = [0, 0, -1, 1];
    
    for (let k = 0; k < 4; k++) {
        let [si, sj] = [i, j];
        
        si += di[k];
        sj += dj[k];
        
        if (si < 0 || si >= 5 || sj < 0 || sj >= 5) continue;
        
        if (board[si][sj] === 'P') {
            answer = false;
            break;
        }
        
        const ni = si + di[k];
        const nj = sj + dj[k];
        
        if (ni < 0 || ni >= 5 || nj < 0 || nj >= 5) continue;
        
        if (board[ni][nj] === 'P') {
            if (board[si][sj] === 'O') {
                answer = false;
                break;
            }
        }
    }
    
    if (!answer) return answer;
    
    // 대각선 cnt 1까지
    const fi = [-1, -1, 1, 1];
    const fj = [-1, 1, -1, 1];
    
    for (let k = 0; k < 4; k++) {
        const ni = i + fi[k];
        const nj = j + fj[k];
        if (ni < 0 || ni >= 5 || nj < 0 || nj >= 5) continue;
        
        if (board[ni][nj] === 'P' && (board[i][nj] === 'O' || board[ni][j] === 'O')) {
            answer = false;
            break;
        }
    }
    return answer
}