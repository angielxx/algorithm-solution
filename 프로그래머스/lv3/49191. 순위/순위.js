function solution(n, results) {
    const graph = Array.from({length:n+1} , _ => Array.from({length:n+1}, _ => 0));
    
    for (const [a, b] of results) {
        graph[a][b] = 1
        graph[b][a] = -1
    }
    
    for (let i = 1; i <= n; i++) {
        for (let j = 1; j <= n; j++) {
            for(let k = 1; k <=n; k++) {
                if (graph[i][j] == 1 && graph[j][k] == 1) {
                    graph[i][k] = 1;
                    graph[k][i] = -1;
                }
                if (graph[i][j] === -1 && graph[j][k] === -1) {
                    graph[i][k] = -1;
                    graph[k][i] = 1;
                }
            }
        }
    }

    let answer = 0;
    for (let i = 1; i <= n; i++) {
        const arr = graph[i].filter((x, idx) => idx !== i && idx !== 0);
        if (arr.every(x => x !== 0)) answer++
    }
    return answer
}