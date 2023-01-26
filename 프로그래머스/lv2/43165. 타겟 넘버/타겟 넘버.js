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
    if (this.head === null) {
      this.head = newNode;
    } else {
      this.tail.next = newNode;
    }

    this.tail = newNode;
    this.size++;
  }
  popleft() {
    const popedNode = this.head;
    this.head = popedNode.next;
    this.size--;
    return popedNode;
  }
  print() {
    let current = this.head;
    while (current) {
      console.log(current.val);
      current = current.next;
    }
  }
}
function solution(numbers, target) {
  let answer = 0;

  // (depth, total)
  let Q = new Queue();
  Q.push([0, numbers[0]]);
  Q.push([0, -1 * numbers[0]]);

  while (Q.size) {
    const [depth, total] = Q.popleft().val;
    if (depth + 1 < numbers.length) {
      Q.push([depth + 1, total + numbers[depth + 1]]);
      Q.push([depth + 1, total - numbers[depth + 1]]);
    } else {
      if (total === target) answer++;
    }
  }

  return answer;
}