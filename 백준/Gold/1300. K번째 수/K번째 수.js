const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let [n, k] = [0, 0];
let count = 2;
rl.on('line', function (line) {
  if (count === 2) {
    n = parseInt(line);
  } else if (count === 1) {
    k = parseInt(line);
  }
  count--;
  if (count === 0) rl.close();
}).on('close', function () {
  let left = 1;
  let right = n * n;
  let answer = 0;

  while (left <= right) {
    const mid = parseInt((left + right) / 2);

    let cnt = 0;
    for (let i = 1; i <= n; i++) {
      cnt += Math.min(parseInt(mid / i), n);
    }

    if (cnt >= k) {
      right = mid - 1;
      answer = mid;
    } else {
      left = mid + 1;
    }
  }
  console.log(answer);
  process.exit();
});
