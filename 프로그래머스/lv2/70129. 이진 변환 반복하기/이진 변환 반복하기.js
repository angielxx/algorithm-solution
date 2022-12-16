function solution(s) {
  let zero = 0
  let cnt = 0
  while (s !== '1') {
    cnt++
    let arr = Array.from(s)
    zero += arr.filter((x) => x === '0').length
    s = arr
      .filter((x) => x === '1')
      .join('')
      .length.toString(2)
  }
  return [cnt, zero]
}
