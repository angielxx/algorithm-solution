function solution(x, n) {
    let result = [];
    const plus = x;
    while (result.length < n) {
        result.push(x);
        x += plus;
    }
    return result
}