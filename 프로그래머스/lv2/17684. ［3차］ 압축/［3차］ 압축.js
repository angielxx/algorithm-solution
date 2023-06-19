function solution(msg) {
    const dict = {A:1, B:2, C:3, D:4, E:5, F:6, G:7, H:8, I:9, J:10, K:11, L:12, M:13, N:14, O:15, P:16, Q:17, R:18, S:19, T:20, U:21, V:22, W:23, X:24, Y:25, Z:26 }
    let next = 27

    const answer = [];
    let i = 0;
    while (i < msg.length) {
        let e = i + 1;
        
        while (e <= msg.length) {
            const w = msg.slice(i, e);
            if (dict[w]) e++;
            else {
                e--;
                break;
            }
        }
        const w = msg.slice(i, e);
        const c = msg.slice(e, e+1);

        if (dict[w]) {
            answer.push(dict[w]);
            dict[w + c] = next;
            next++;
        }

        i = e;
        if (c === '') break;
    }
    return answer
}