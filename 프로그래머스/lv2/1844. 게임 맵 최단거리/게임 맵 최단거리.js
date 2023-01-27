function solution(maps) {
  const [n, m] = [maps.length, maps[0].length];

  const di = [-1, 1, 0, 0];
  const dj = [0, 0, -1, 1];

  Q = new Queue();
  Q.push([0, 0]);

  while (Q.size) {
    const [si, sj] = Q.popleft().val;

    for (let k = 0; k < 4; k++) {
      const ni = si + di[k];
      const nj = sj + dj[k];

      if (ni >= 0 && ni < n && nj >= 0 && nj < m && maps[ni][nj] === 1) {
        maps[ni][nj] = maps[si][sj] + 1;
        Q.push([ni, nj]);
      }
    }
  }

  if (maps[n - 1][m - 1] === 1) return -1;
  else return maps[n - 1][m - 1];
}

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
      this.tail = this.head;
    } else {
      this.tail.next = newNode;
      this.tail = newNode;
    }
    this.size++;
  }

  popleft() {
    if (!this.size) {
      return null;
    }
    const popedNode = this.head;
    this.head = this.head.next;
    this.size--;
    return popedNode;
  }
  print() {
    console.log("start print");
    let currentNode = this.head;
    while (currentNode) {
      console.log(currentNode);
      currentNode = currentNode.next;
    }
    console.log("end print");
  }
}