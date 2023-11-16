class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
    this.prev = null;
  }
}

function solution(n, k, cmd) {
  let selected;
  const history = [];
  const answer = Array.from({ length: n }, (_) => 'O');

  let prevNode = new Node(0);

  for (let i = 1; i < n; i++) {
    const currNode = new Node(i);
    currNode.prev = prevNode;
    prevNode.next = currNode;
    prevNode = currNode;

    if (i === k) {
      selected = currNode;
    }
  }

  function u(cnt) {
    while (selected.prev && cnt) {
      cnt--;
      k--;
      selected = selected.prev;
    }
  }
  function d(cnt) {
    while (selected.next && cnt) {
      cnt--;
      k++;
      selected = selected.next;
    }
  }
  function c() {
    const prev = selected.prev;
    const next = selected.next;

    history.push(selected);
    answer[selected.val] = 'X';

    if (prev) prev.next = next;
    if (next) next.prev = prev;

    selected = next ? next : prev;
  }
  function z() {
    const recover = history.pop();
    answer[recover.val] = 'O';

    const prev = recover.prev;
    const next = recover.next;
    if (prev) prev.next = recover;
    if (next) next.prev = recover;
  }

  for (let cm of cmd) {
    if (cm.startsWith('U')) {
      const cnt = cm.split(' ').map(Number)[1];
      u(cnt);
    }
    if (cm.startsWith('D')) {
      const cnt = cm.split(' ').map(Number)[1];
      d(cnt);
    }
    if (cm === 'C') c();
    if (cm === 'Z') z();
  }
  return answer.join('');
}