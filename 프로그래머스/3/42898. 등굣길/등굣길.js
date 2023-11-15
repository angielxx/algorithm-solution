function solution(m, n, puddles) {    
    const water = Array.from({length:n+1}, _=> Array.from({length:m+1}, _=>0));
    for (const [i, j] of puddles) {
        water[j][i] = 1;
    }

    const dp = Array.from({length:n+1}, _=>Array.from({length:m+1}, _=> 0));
    dp[1][1] = 1
    
    for (let i = 1; i < n+1; i++) {
        for (let j = 1; j < m+1; j++) {
            if (i === 1 && j === 1) continue;
            if (water[i][j]) dp[i][j] = 0;
            else {
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000007
            }
        }
    }
    
    return dp[n][m]
}