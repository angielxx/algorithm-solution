function solution(arrayA, arrayB) {
    
    const divA = arrayA.reduce((a, b) => gcd(a, b));
    const divB = arrayB.reduce((a, b) => gcd(a, b));
    console.log(divA, divB);
    
    const isA = arrayB.every((x) => x / divA !== Math.floor(x / divA));
    const isB = arrayA.every((x) => x / divB !== Math.floor(x / divB));
    
    const answer = [];
    if (isA) answer.push(divA);
    if (isB) answer.push(divB);
    
    if (!answer.length) return 0;
    return Math.max(...answer);
}

function gcd(a, b) {
    while (b !== 0) {
        const r = a % b;
        a = b;
        b = r;
    }
    return a;
}