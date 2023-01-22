function solution(n) {
  if (n === 1) return 1;
  let dp = Array.from({ length: n + 1 }, (_) => 0);
  dp[0] = 1;
  dp[1] = 1;

  for (let i = 2; i <= n; i++) {
    dp[i] = (dp[i - 1] + dp[i - 2]) % 1234567;
  }
  return dp[n];
}