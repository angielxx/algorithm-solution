function solution(enroll, referral, seller, amount) {
    // 판매 데이터에서 루트까지 타고 올라가야함
    // parent = { child : parent }
    // result = [0, 0,...]
    // idx = {name: i}
    const idx = {};
    const result = Array.from({length: enroll.length}, _ => 0);
    const parent = {};
    
    for (let i = 0; i < enroll.length; i++) {
        const c = enroll[i];
        const p = referral[i];
        parent[c] = p;
        idx[c] = i;
    }
    // console.log(idx)
    // console.log(parent)
    
    for (let i = 0; i < seller.length; i++) {
        let c = seller[i];
        let total = 100 * amount[i];
        // console.log('start :', c, total)
        while (true) {
            if (c === '-') break;
            const p = parent[c];
            const rest = Math.floor(total * 0.1);
            const mine = total - rest;
            // console.log(mine, rest)
            if (rest < 1) {
                // console.log('here', c)
                result[idx[c]] += mine;
                break;
            }
            result[idx[c]] += mine;
            // console.log(c, p, result)
            c = p;
            total = rest;
        }
        // console.log('result :', result)
        // console.log()
    }
    return result
}