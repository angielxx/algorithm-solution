function solution(orders, course) {
    const table = {};
    for (let i = 0; i < orders.length; i++) {
        const order = orders[i];
        for (let s of order) {
            table[s] = table[s] ? [...table[s], i] : [i];
        }
    }
    const alpha = Object.keys(table).sort();
    
    let len = 2;
    let combi = Object.assign({}, table);
    let answer = [];
    while (len <= course[course.length - 1]) {
        const temp = {};
        for (let key of Object.keys(combi).sort()) {
            const val = combi[key];
            if (val.length < 2) continue;
            
            const now = alpha.indexOf(key[key.length - 1]);
            for (let i = now + 1; i < alpha.length; i++) {
                const str = key + alpha[i];
                const next = val.filter((x) => table[alpha[i]].includes(x));
                if (next.length >= 2) temp[str] = next;
            }
        }
        if (course.includes(len)) {
            let max_len = 0;
            let ans = [];
            for (let [key, val] of Object.entries(temp)) {
                if (val.length > max_len) {
                    max_len = val.length;
                    ans = [key]
                } else if (val.length === max_len) {
                    ans.push(key)
                }
            }
            answer.push(...ans)
        }
        combi = Object.assign({}, temp);
        len++;
    }
    return answer.sort()
}