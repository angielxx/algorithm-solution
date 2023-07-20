function solution(arrayA, arrayB) {
    // A의 모든 수의 약수 Set
    // A의 약수에는 있고 B의 약수 중엔 없는 것
    const setA = new Set();
    for (const a of arrayA) {
        console.log(div(a))
        setA.add(...div(a));
        console.log(setA)
    }
    console.log()
}

function div(a) {
    const result = [];
    
    for (let n = 2; n <= Math.floor(Math.sqrt(a)); n++) {
        if (a % n === 0) result.push(n, a/n);
    }
    return result
}