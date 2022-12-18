function solution(n) {
  let arr = Array.from({ length: 100000 }, (_) => 0)
  arr[0] = 0
  arr[1] = 1
  //   console.log(arr.slice(0, 6))
  function fib(n) {
    if (n <= 1) return arr[n]
    if (n >= 2) {
      for (let i = 2; i <= n; i++) {
        arr[i] = (arr[i - 1] + arr[i - 2]) % 1234567
      }
      return arr[n]
    }
  }
  return fib(n)
}