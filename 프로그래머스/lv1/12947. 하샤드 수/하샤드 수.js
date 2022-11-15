function solution(x) {
    let sum = 0;
    x = String(x);
    for (let i = 0; i < x.length; i++) {
        sum += Number(x[i])
    }
    if (Number(x) % sum === 0) return true;
    else return false;
}