function solution(board) {
    // 위, 왼쪽, 대각
    const di = [-1, 0, -1];
    const dj = [0, -1, -1];
    
    for (let i = 0; i < board.length; i++) {
        for (let j = 0; j < board[0].length; j++) {
            if (board[i][j] === 1) {
                const temp = [];
                let flag = true;
                for (let k = 0; k < 3; k++) {
                    const ni = i + di[k];
                    const nj = j + dj[k];
                    if (ni < 0 || ni >= board.length || nj < 0 || nj >= board[0].length) {
                        flag = false;
                        break;
                    }
                    temp.push(board[ni][nj]);
                }
                if (flag) {
                    board[i][j] = Math.min(...temp) + 1;
                }
            }
        }
    }
        
    let answer = 0;
    for (let arr of board) {
        answer = Math.max(answer, ...arr)
    }
    return answer ** 2
}