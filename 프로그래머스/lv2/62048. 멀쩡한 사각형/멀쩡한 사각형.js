function solution(w, h) {    
    const n = gcd(w, h);
    const [a, b] = [w / n, h / n];
    const m = a * b - (a - 1) * (b - 1);

    return w * h - m * n;
}

function gcd(a, b) {
    while (b !== 0) {
        const r = a % b;
        a = b;
        b = r;
    }
    return a
}