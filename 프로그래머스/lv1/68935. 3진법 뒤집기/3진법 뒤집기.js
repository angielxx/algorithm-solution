function solution(n) {
  // 10 -> 3
  let three = ''
  while (n > 0) {
    r = n % 3
    n = parseInt(n / 3)
    three += String(r)
  }
  three = three.split('').reverse().join('')

  // 3 -> 10
  let arr = Array.from(three).map(Number)

  let answer = 0
  arr.forEach((val, idx) => (answer += 3 ** idx * val))
  return answer
}
