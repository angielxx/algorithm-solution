function solution(triangle) {
    // dp[i][j][0, 0] 왼쪽에서 내려온 경우, 오른쪽에서 내려온 경우
    const dp = Array.from({length:triangle.length}, (_,i) => Array.from({length:i+1}, (_, j) => 0));
    dp[0][0] = triangle[0][0];
    
    for (let i = 1; i < triangle.length; i++) {
        for (let j = 0; j < i+1; j++) {
            if (j === 0) {
                dp[i][j] = dp[i-1][0] + triangle[i][j];
            }
            else if (j === i) {
                dp[i][j] = dp[i-1][i-1] + triangle[i][j];
            }
            else {
                dp[i][j] = triangle[i][j] + Math.max(dp[i-1][j-1], dp[i-1][j]);
            }
        }
    }
    return Math.max(...dp[triangle.length - 1])
}