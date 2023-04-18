function check(user, ban) {
    for (let i = 0; i < user.length; i++) {
        if (ban[i] === '*') continue;
        else if (ban[i] !== '*' && ban[i] === user[i]) continue;
        else if (ban[i] !== '*' && ban[i] !== user[i]) return false;
    }
    return true;
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
}

function solution(user_id, banned_id) {
    // obj = {} -> bannner_id : [user, ...]
    // bfs
    let cnt = [];
    
    const obj = {};
    const visited = new Map();
    
    for (let i = 0; i < banned_id.length; i++) {
        const ban = banned_id[i];
        for (let j = 0; j < user_id.length; j++) {
            const user = user_id[j];
            visited.set(user, false)
            
            if (ban.length !== user.length) continue;
            if (check(user, ban)) {
                if (obj[ban] && obj[ban].includes(user)) continue;
                obj[ban] = obj[ban]? [...obj[ban], user] : [user]
            }
        }
    }
    
    // 0 = index
    function bfs(index, visited, depth) {
        q = new Queue;
        q.push([index, []]);

        while (q.size) {
            const [idx, arr] = q.popleft();
            if (idx === depth) {
                cnt.push(arr.sort().join(','))
                continue;
            }

            const next_arr = obj[banned_id[idx]]? obj[banned_id[idx]]: [];
            if (next_arr.length === 0) continue;
            for (let next of next_arr) {
                if (!arr.includes(next)) q.push([idx + 1, [...arr, next]])
            }
        }  
    }
    
    bfs(0, visited, banned_id.length)
    const set = new Set(cnt);
    return set.size;
}