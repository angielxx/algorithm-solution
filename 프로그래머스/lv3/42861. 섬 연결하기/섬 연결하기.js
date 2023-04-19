function solution(n, costs) {
    
    function find_set(x) {
        while (x !== rep[x]) {
            x = rep[x]
        }
        return x
    }
    
    function union(x, y) {
        rep[find_set(y)] = find_set(x);
    }
    
    costs.sort((a, b) => a[2] - b[2])
    
    const rep = Array.from({length : n}, (a, b) => b);
    
    let cnt = 0;
    let total = 0;
    for (let [u, v, w] of costs) {
        if (find_set(u) !== find_set(v)) {
            cnt++;
            union(u, v);
            total += w;
            if (cnt === n) break;
        }
    }
    return total
}