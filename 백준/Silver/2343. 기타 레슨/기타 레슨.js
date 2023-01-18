const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");

const [n, m] = Array.from(input[0].trim().split(" ")).map(Number);
const arr = Array.from(input[1].split(" ")).map(Number);

let [left, right] = [Math.max(...arr), arr.reduce((a, b) => a + b)];
let answer;

while (left <= right) {
  let mid = Math.floor((left + right) / 2);

  let [cnt, total] = [1, 0];
  for (let i = 0; i < n; i++) {
    total += arr[i];
    if (total > mid) {
      cnt++;
      total = arr[i];
    }
  }
  if (cnt <= m) {
    answer = mid;
    right = mid - 1;
  } else {
    left = mid + 1;
  }
}

console.log(answer);
