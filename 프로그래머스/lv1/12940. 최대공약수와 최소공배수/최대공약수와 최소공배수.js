function solution(n, m) {
    // b < a
    let a;
    let b;
    if (n <= m) {
        b = n
        a = m
    } else {
        b = m
        a = n
    }
    // 최대공약수
    function gcd(a, b) {
        while (b !== 0) {
            let r = a % b;
            a = b
            b = r
        }
        return a;
    }
    // 최소공배수
    function lcm(a, b) {
        return a * b / gcd(a, b)
    }

    return [gcd(a, b), lcm(a,b)]
}