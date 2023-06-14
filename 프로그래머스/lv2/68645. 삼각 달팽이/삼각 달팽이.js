function solution(n) {
    // 0 1 2 3 4 5 6 7 8 9 (1 + 2 + 3 + 4)
    /*
    
    1 2 3 4 5 / 6 7 8 9 / 10 11 12 / 13 14 / 15 - 5회 (k = 0 ~ 4)
    5 4 3 2 1 = n - k (원소 개수)
    k % 3 === 0, 1, 2 - 각 하 우 상
    */
    
    /*
    Array(n).fill(Array(n).fill) -> 이렇게 2차원 배열 만들면 내부 배열이 동일한 참조값을 가짐
    */
    const arr = Array.from({length: n}, _ => Array.from({length:n}, _ => 0));
    
    let x = -1;
    let y = 0;
    let val = 1;
    
    for (let k = 0; k < n; k++) {
        for (let l = n - k; l > 0; l--) {
            // down
            if (k % 3 === 0) {
                x++;
            };
            // right
            if (k % 3 === 1) {
                y++;
            };
            //up
            if (k % 3 === 2) {
                x--;
                y--;
            };
            arr[x][y] = val;
            val++;
        }
    }
    const answer = [];
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < i + 1; j++ ) {
            answer.push(arr[i][j])
        }
    }
    return answer
}