function solution(n) {
  let a = 0
  let b = 1
  let f = 1
  for (let i = 2; i <= n; i++) {
    f = (a + b) % 1234567
    a = b
    b = f
  }
  return f
}
