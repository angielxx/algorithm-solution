function solution(data, col, row_begin, row_end) {
    data.sort((a, b) => {
        const x = a[col - 1] - b[col - 1];
        if (x) return x
        return b[0] - a[0]
    });
    
    const S = Array.from({length:data.length}, _=> 0);
    
    data.forEach((item, idx) => {
        let s = 0;
        item.forEach((n) => s += (n % (idx + 1)));
        S[idx] = s
    })
    console.log(S)
    console.log(S.slice(row_begin - 1, row_end))
    const answer = S.slice(row_begin - 1, row_end).reduce((a, b) => a ^ b, 0);
    
    return answer;
}