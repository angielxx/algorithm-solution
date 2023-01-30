/*
방문하지 않은 노드라면 bfs를 시작
방문하지 않은 노드 발견할 때마다 네트워크 개수 +1
*/
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
    const popedNode = this.head;
    this.head = this.head.next;
    this.size--;
    return popedNode;
  }
  print() {
    let currentNode = this.head;
    console.log("print start");
    while (currentNode) {
      console.log(currentNode);
      currentNode = currentNode.next;
    }
    console.log("print end");
    console.log();
  }
}

function solution(n, computers) {
  let visited = Array.from({ length: n }, (_) => 0);
  // 네트워크 개수
  let network = 0;
  for (let i = 0; i < n; i++) {
    // 방문하지 않은 노드라면 bfs 시작
    if (visited[i] === 0) {
      network++;
      Q = new Queue();
      Q.push(i);
      while (Q.size) {
        const now = Q.popleft().val;
        visited[now] = 1;
        // now 컴퓨터와 연결된 컴퓨터들
        const adj = computers[now];
        adj.forEach((x, id) => {
          if (id !== now && visited[id] === 0 && x === 1) {
            Q.push(id);
          }
        });
      }
    }
  }
  return network;
}