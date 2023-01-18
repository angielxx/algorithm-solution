const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");

/*
jealous = INF
7 4
cnt = 2
*/

const [n, m] = Array.from(input[0].trim().split(" ")).map(Number);
let arr = [];
for (let i = 1; i < input.length; i++) {
  arr.push(input[i].trim());
}
arr = arr.map(Number);

// 탐색할 수를 기준으로 left, right를 정한다.
// 이 문제의 경우 나눠줄 보석의 수
let [left, right] = [1, Math.max(...arr)];

let jealous = 10 ** 9;
while (left <= right) {
  let mid = Math.ceil((left + right) / 2);

  // 나누어지는 갯수
  let cnt = 0;
  for (let i = 0; i < m; i++) {
    cnt += Math.ceil(arr[i] / mid);
  }
  if (cnt <= n) {
    jealous = Math.min(jealous, mid);
    right = mid - 1;
  } else {
    left = mid + 1;
  }
}
console.log(jealous);
