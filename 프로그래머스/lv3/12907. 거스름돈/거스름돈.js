function solution(n, money) {
    const dp = [1, ...Array(n).fill(0)];
    
    for (let coin of money) {
        for (let price = coin; price <= n; price++) {
            if (price >= coin) dp[price] += dp[price - coin];
        }
    }
    return dp[n] % 1000000007
}