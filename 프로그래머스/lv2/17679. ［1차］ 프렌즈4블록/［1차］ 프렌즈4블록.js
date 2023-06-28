function solution(m, n, board) {
    // 90도로 돌리기
    let b = [];
    for (let j = 0; j < board[0].length; j++) {
        let str = '';
        for (let i = 0; i < board.length; i++) {
            str += board[i][j];
        }
        b.push(str);
    }

    let answer = 0;
    while (true) {
        // for (let r of b) {
        //     console.log(r)
        // }
        let toRemove = Array.from({length:b.length}, _ => Array.from({length:b[0].length}, _ => 0));
        
        for (let i = 0; i <= b.length - 2; i++) {
            for (let j = 0; j <= b[0].length -2; j++) {
                if (b[i][j] == '0') continue;
                if (isSame(i, j, b)) {
                    toRemove = check(i, j, toRemove);
                }
            }
        }
        let num = 0;
        toRemove.forEach((row) => num += row.filter(x => x === 1).length);
        
        if (!num) break;
        answer += num;
        
        b = remove(toRemove, b)
    }
    return answer
}

function remove(toRemove, b) {
    const arr = [];
    for (let i = 0; i < toRemove.length; i++) {
        let str = '';
        for (let j = 0; j < toRemove[0].length; j++) {
            if (!toRemove[i][j]) str += b[i][j];
        }
        if (str.length < toRemove.length) str = `${Array(toRemove.length - str.length).fill(0).join('')}` + str
        arr.push(str)
    }
    // console.log(arr)
    return arr
}

function isSame(i, j, b) {
    const bl = b[i][j];
    let flag = true;
    for (let k = i; k < i + 2; k++) {
        for (let l = j; l < j + 2; l++) {
            if (b[k][l] !== bl) {
                flag = false;
                break;
            }
        }
    }
    return flag
}
    
function check(i, j, toRemove) {
    for (let k = i; k < i + 2; k++) {
        for (let l = j; l < j + 2; l++) {
            toRemove[k][l] = 1;
        }
    }
    return toRemove
}
    
