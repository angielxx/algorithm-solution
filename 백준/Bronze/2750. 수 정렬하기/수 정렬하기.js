const fs = require('fs')
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')
//let input = fs.readFileSync('example.txt').toString().trim().split('\n')

const N = Number(input[0])
const arr = input.slice(1).map(Number)

// function bubbleSort(arr) {
//   // i : 교환하는 범위의 맨 마지막 원소의 인덱스
//   for (let i = arr.length; i > 0; i--) {
//     // j : 교환하는 범위의 첫번째 원소의 인덱스
//     for (let j = 0; j < i - 1; j++) {
//       if (arr[j] > arr[j + 1]) {
//         let temp = arr[j]
//         arr[j] = arr[j + 1]
//         arr[j + 1] = temp
//       }
//     }
//   }
//   return arr
// }

// bubbleSort(arr)

function selectionSort(arr) {
  for (let i = 0; i < arr.length; i++) {
    let MIN = i
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[j] < arr[MIN]) {
        MIN = j
      }
    }
    if (i !== MIN) {
      let temp = arr[i]
      arr[i] = arr[MIN]
      arr[MIN] = temp
    }
  }
  return arr
}
selectionSort(arr)
for (let i = 0; i < arr.length; i++) {
  console.log(arr[i])
}
