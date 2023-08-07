let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const [a, b, c] = input.map(Number);
const number = String(a * b * c);

const answer = Array(10).fill(0);

for (let i = 0; i < number.length; i++) {
  const str = number[i];
  answer[str]++;
}

for (const a of answer) {
  console.log(a);
}
