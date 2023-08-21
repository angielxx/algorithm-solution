const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : 'input.txt';
let input = fs.readFileSync(filePath).toString().trim().split('\n');

const [n, m] = input[0].split(' ');
let arr = input.splice(1).map((li) => li.split(' ').map(Number));

class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

class Queue {
  constructor() {
    this.size = 0;
    this.head = null;
    this.tail = null;
  }
  push(val) {
    const newNode = new Node(val);
    if (!this.head) {
      this.head = newNode;
    } else {
      this.tail.next = newNode;
    }
    this.tail = newNode;
    this.size++;
  }
  shift() {
    if (!this.head) return;
    const theNode = this.head;
    this.head = theNode.next;
    this.size--;
    return theNode.val;
  }
  print() {
    let theNode = this.head;
    while (theNode) {
      console.log(theNode);
      theNode = theNode.next;
    }
  }
}

const di = [-1, 1, 0, 0];
const dj = [0, 0, -1, 1];

let answer = 0;

while (true) {
  const temp = Array.from({ length: n }, (_) =>
    Array.from({ length: m }, (_) => 0)
  );
  const visited = Array.from({ length: n }, (_) =>
    Array.from({ length: m }, (_) => 0)
  );

  function bfs(i, j) {
    const q = new Queue();
    q.push([i, j]);
    visited[i][j] = 1;
    while (q.size) {
      const [si, sj] = q.shift();
      cnt = 0;
      for (let k = 0; k < 4; k++) {
        const ni = si + di[k];
        const nj = sj + dj[k];
        if (arr[ni][nj] === 0) cnt++;
        if (
          0 <= ni < n &&
          0 <= nj < m &&
          visited[ni][nj] === 0 &&
          arr[ni][nj] !== 0
        ) {
          q.push([ni, nj]);
          visited[ni][nj] = 1;
        }
      }
      temp[si][sj] = Math.max(arr[si][sj] - cnt, 0);
    }
  }

  let island = 0;
  let flag = false;
  let sum = 0;
  for (let i = 0; i < n; i++) {
    if (flag) break;
    for (let j = 0; j < m; j++) {
      sum += arr[i][j];
      if (arr[i][j] && !visited[i][j]) {
        island++;
        bfs(i, j);
      }
      if (island > 1) {
        flag = true;
        break;
      }
    }
  }
  if (sum === 0) {
    answer = 0;
    break;
  }

  if (island > 1) {
    break;
  } else {
    arr = temp;
    answer += 1;
  }
}

console.log(answer);
