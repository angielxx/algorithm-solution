const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : 'input.txt';
let input = fs.readFileSync(filePath).toString().trim().split('\n');

const [n, m] = input[0].split(' ').map(Number);
const arr = input.splice(1);

const di = [-1, 1, 0, 0];
const dj = [0, 0, -1, 1];

class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

class Queue {
  constructor() {
    this.head = null;
    this.tail = null;
    this.size = 0;
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
    let node = this.head;
    while (node) {
      console.log(node);
      node = node.next;
    }
  }
}

// [i][j][0, 1]  - 벽을 안 부순 경우, 부순 경우 두 가지 경우의 수에 대해 각각 방문처리
const visited = Array.from({ length: n }, (_) =>
  Array.from({ length: m }, (_) => Array.from({ length: 2 }, (_) => 0))
);

const q = new Queue();
q.push([0, 0, 0, 1]);
visited[0][0] = 1;

let flag = false;

while (q.size > 0) {
  const [i, j, isBroke, distance] = q.shift();

  if (i === n - 1 && j === m - 1) {
    console.log(distance);
    flag = true;
    break;
  }

  for (let k = 0; k < 4; k++) {
    const ni = i + di[k];
    const nj = j + dj[k];

    if (ni < 0 || ni >= n || nj < 0 || nj >= m) {
      continue;
    }
    if (isBroke && visited[ni][nj][1] === 1) continue;
    if (!isBroke && visited[ni][nj][0] === 1) continue;

    // 벽이 아닌 경우
    if (arr[ni][nj] === '0') {
      q.push([ni, nj, isBroke, distance + 1]);
      if (isBroke) visited[ni][nj][1] = 1; // 부순 경우
      else visited[ni][nj][0] = 1; // 안 부순 경우
    }
    // 벽인 경우 & 부수고 지나갈 수 있는 경우
    if (arr[ni][nj] === '1' && isBroke === 0) {
      q.push([ni, nj, 1, distance + 1]);
      visited[ni][nj][1] = 1; // 부순 경우
    }
  }
}

if (!flag) {
  console.log(-1);
}
