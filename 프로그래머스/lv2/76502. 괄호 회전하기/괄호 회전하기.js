function solution(s) {
  class Node {
    constructor(val) {
      this.val = val;
      this.next = null;
    }
  }
  class Queue {
    constructor() {
      this.first = null;
      this.last = null;
      this.size = 0;
    }

    enqueue(val) {
      const newNode = new Node(val);
      if (!this.first) {
        this.first = newNode;
        this.last = newNode;
      } else {
        this.last.next = newNode;
        this.last = newNode;
      }
      return ++this.size;
    }

    dequeue() {
      if (!this.first) return null;

      const temp = this.first;
      if (this.first === this.last) {
        this.last = null;
      }
      this.first = this.first.next;
      this.size--;
      return temp.val;
    }
    isEmpty() {
      if (!this.size) return true;
      else return false;
    }
    getFirst() {
      return this.first;
    }
  }

  const arr = Array.from(s);
  let Q = new Queue();
  arr.forEach((x) => Q.enqueue(x));

  pair = {
    ")": "(",
    "]": "[",
    "}": "{",
  };

  let cnt = 0;
  let answer = 0;
  while (cnt < arr.length) {
    cnt++;
    const temp = Q.dequeue();
    Q.enqueue(temp);

    let check = new Queue();
    firstNode = Q.getFirst();
    check.enqueue(firstNode.val);
    while (firstNode.next) {
      check.enqueue(firstNode.next.val);
      firstNode = firstNode.next;
    }

    let stack = [];
    let flag = true;
    while (check.size) {
      // console.log("cnt :", cnt, "check :", check);
      // console.log(stack);
      const el = check.dequeue();
      if (["(", "{", "["].includes(el) || !stack.length) {
        stack.push(el);
      } else if ([")", "]", "}"].includes(el)) {
        if (stack[stack.length - 1] == pair[el]) {
          stack.pop();
        } else {
          flag = false;
          break;
        }
      }
    }
    if (stack.length) {
      flag = false;
    }
    if (flag) {
      answer++;
    }
  }
  return answer;
}