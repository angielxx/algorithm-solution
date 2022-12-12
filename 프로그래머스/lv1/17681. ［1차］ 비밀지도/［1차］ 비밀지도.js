function solution(n, arr1, arr2) {
  function decToBin(num) {
    num = num.toString(2)
    if (num.length < n) {
      num = '0'.repeat(n - num.length) + num
    }
    return num
  }
  arr1 = arr1.map(decToBin)
  arr2 = arr2.map(decToBin)

  let answer = []
  for (let i = 0; i < n; i++) {
    let el = ''
    for (let j = 0; j < n; j++) {
      if (arr1[i][j] == '1' || arr2[i][j] == '1') el += '1'
      else el += '0'
    }
    answer.push(el)
  }
  answer = answer.map((el) => {
    let newEl = ''
    for (let i = 0; i < n; i++) {
      if (el[i] == '1') newEl += '#'
      else newEl += ' '
    }
    return newEl
  })
  return answer
}