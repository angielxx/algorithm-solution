class Node {
    constructor(val) {
        this.val = val;
        this.next = null;
    }
}

class Queue {
    constructor() {
        this.length = 0;
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
        this.length += 1;
    }
    
    pop() {
        if (!this.head) return
        
        const poped = this.head;
        this.head = this.head.next;
        this.length--;
        return poped.val;
    }
    
    print() {
        const q = [];
        if (!this.length) {
            console.log(q)
            return q;
        }
        
        let node = this.head;
        while (node.next) {
            q.push(node.val);
        }
        console.log(q)
        return q
    }
}

function solution(maps) {
    // 상, 하, 좌, 우
    const di = [0, 0, -1, 1];
    const dj = [-1, 1, 0, 0];
    
    let start;
    let lever;
    let exit;
    
    const h = maps.length;
    const w = maps[0].length;
    
    for (let i = 0; i < h; i++) {
        for (let j = 0; j < w; j++) {
            if (maps[i][j] === 'S') start = [i, j];
            if (maps[i][j] === 'L') lever = [i, j];
            if (maps[i][j] === 'E') exit = [i, j];
        }
    }
    
    let answer = 0;
    const check = [0,0]
    // 3차원 배열 visited[][][S -> L, E -> S]
    const visited = Array.from({length:h}, _ => Array.from({length:w}, _ => Array.from({length:2}, _ => false)));
    

    let Q = new Queue();
    Q.push([...start, 0, 'S'])
    Q.push([...exit, 0, 'E'])
    
    while (Q.length) {
        const [si, sj, t, start_point] = Q.pop();
        // console.log(si, sj, t, start_point)
        
        if (start_point === 'S' && maps[si][sj] === 'L') {
            answer += t;
            check[0] = 1;
            continue;
        }
        if (start_point === 'E' && maps[si][sj] === 'L') {
            answer += t;
            check[1] = 1;
            continue;
        }
        
        for (let k = 0; k < 4; k++) {
            const ni = si + di[k];
            const nj = sj + dj[k];
            
            if (ni < 0  || ni >= h || nj < 0 || nj >= w || maps[ni][nj] === 'X' ) continue
            if (start_point === 'S' && visited[ni][nj][0]) continue;
            if (start_point === 'E' && visited[ni][nj][1]) continue;
            
            Q.push([ni, nj, t + 1, start_point]);
            
            if (start_point === 'S') visited[ni][nj][0] = true;
            else visited[ni][nj][1] = true;
        }
    }
    if (check[0] + check[1] < 2) return -1
    
    return answer
}