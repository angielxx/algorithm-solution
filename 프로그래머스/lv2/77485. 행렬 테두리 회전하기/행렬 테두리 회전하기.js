function solution(rows, columns, queries) {
    const arr = Array.from({length: rows}, (x, i) => Array.from({length: columns}, (y, j) => columns * i + j + 1 ));
    
    const answer = [];
    for (const query of queries) {
        const [x1, y1, x2, y2] = query;
        const min = rotate(arr, x1, y1, x2, y2);
        answer.push(min)
    }
    return answer
}

function rotate(arr, x1, y1, x2, y2) {
    // 시계방향으로 우, 하, 좌, 상
    const di = [0, 1, 0, -1];
    const dj = [1, 0, -1, 0];
    
    const candidates = [];
    let k = 0;
    let i = x1 - 1;
    let j = y1 - 1;

    while (true) {
        candidates.push(arr[i][j]);
        i += di[k];
        j += dj[k];
        if (k === 0) {
            if (j === y2) {
                k++;
                j--;
                i++;
            }            
        }
        else if (k === 1) {
            if (i === x2) {
                k++;
                i--;
                j--;
            }
        }
        else if (k === 2) {
            if (j === y1 - 2) {
                k++;
                i--;
                j++;
            }
        }
        else if (k === 3) {
            if (i === x1 - 2) {
                candidates.pop();
                break;
            }
        }
    }

    i = x1 - 1;
    j = y1;
    k = 0;
    let idx = 0;
    while (true) {
        arr[i][j] = candidates[idx];
        i += di[k];
        j += dj[k];
        idx++;
        if (k === 0) {
            if (j === y2) {
                k++;
                j--;
                i++;
            }            
        }
        else if (k === 1) {
            if (i === x2) {
                k++;
                i--;
                j--;
            }
        }
        else if (k === 2) {
            if (j === y1 - 2) {
                k++;
                i--;
                j++;
            }
        }
        else if (k === 3) {
            if (i === x1 - 2) {
                break;
            }
        }
    }
    arr[x1 - 1][y1 - 1] = candidates[candidates.length - 1];

    return Math.min(...candidates)
}