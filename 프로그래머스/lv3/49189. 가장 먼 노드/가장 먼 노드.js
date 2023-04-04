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
        } 
        else {
            this.tail.next = node;
        }
        this.tail = node;
        this.size++;
    }
    
    shift() {
        if (!this.head) return undefined;
        const poped = this.head;
        this.head = poped.next;
        this.size--;
        return poped
    }
    
    print() {
        console.log('print start')
        let node = this.head;
        while (node.next !== null) {
            console.log(node);
            node = node.next;
        }
        console.log('print end')
        console.log()
    }
     
    isEmpty() {
        if (this.size) return false;
        return true;
    }
}

function solution(n, edge) {
    // 인접 리스트 만들기
    const adj = {};
    // 거리 테이블
    const distance = {};
    
    for (let i = 0; i < edge.length; i++) {
        const [a, b] = edge[i];
        adj[a] = adj[a] ? [...adj[a], b] : [b];
        adj[b] = adj[b] ? [...adj[b], a] : [a];
    }
    
    const visited = Array.from({length:n}, _ => false);
    
    function bfs(start) {
        const q = new Queue();
        q.push([start, 0]);  // 노드번호, 거리
        visited[start] = true;

        while (!q.isEmpty()) {
            const a = q.shift().val;
            const [now, depth] = a;
            distance[depth] = distance[depth] ? [...distance[depth], now] : [now]
            
            for (let next of adj[now]) {
                if (!visited[next]) {
                    q.push([next, depth + 1])
                    visited[next] = true;
                };
            }
            
        }
    }
    
    bfs(1);
    const key = Object.keys(distance);
    const max = key[key.length - 1];

    return distance[max].length
}

