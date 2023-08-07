let fs = require('fs')
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')
// let input = fs.readFileSync('example.txt').toString().trim().split('\n')

const maxNum = Number(input[2])
const arr = input[1]
  .split(' ')
  .map(Number)
  .sort((a, b) => a - b)

let s = 0
let e = Number(input[0]) - 1
let cnt = 0

while (s < e) {
  let num = arr[s] + arr[e]
  if (num == maxNum) {
    cnt += 1
    s += 1
  } else if (num < maxNum) {
    s += 1
  } else {
    e -= 1
  }
}

console.log(cnt)
