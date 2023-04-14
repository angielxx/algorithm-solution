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
        const node = new Node(val);
        if (!this.head) {
            this.head = node;
        } else {
            this.tail.next = node;
        }
        this.tail = node;
        this.size++;
    }
    
    popleft() {
        const poped = this.head;
        this.head = poped.next;
        this.size--;
        return poped.val;
    }
    
    print() {
        console.log('start print');
        let now = this.head;
        while (now.next) {
            console.log(now);
            now = now.next;
        }
    }
} 

// function bfs(start, n, adj) {
//     const q = new Queue();
//     q.push(start);
    
//     while (q.size) {
//         const now = q.popleft();
//         const nextArr = adj.get(now);
//         for (let next of nextArr) {
//             if (!visited[next])
//         }
//     }
// }

function solution(n, wires) {
    const adj = new Map();
    for (let wire of wires) {
        const [a, b] = wire;
        adj.set(a, adj.get(a)? [...adj.get(a), b] : [b]);
        adj.set(b, adj.get(b)? [...adj.get(b), a] : [a]);
    
    }
    
    let gap = n;
    // 하나씩 끊어보기
    for (let wire of wires) {
        // 갈 수 없는 경로
        const [a, b] = wire;
        
        const visited = Array.from({ length : n + 1 }, _ => false);
        const trees = [];
        for (let i = 1; i <= n; i++) {
            // bfs 시작
            if (!visited[i]) {
                const q = new Queue();
                q.push(i);
                visited[i] = true;
                let cnt = 1;

                while (q.size) {
                    const now = q.popleft();
                    const nextArr = adj.get(now);
                    for (let next of nextArr) {
                        if (!visited[next] && !((now === a && next === b) || (now === b && next === a) )) {
                            q.push(next);
                            visited[next] = true;
                            cnt++;
                        }
                    }
                }
                trees.push(cnt)
            }
        }
        gap = Math.min(Math.abs(trees[0] - trees[1]), gap)
    }
    return gap;
}