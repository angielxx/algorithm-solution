function solution(n, k) {
    const changed = n.toString(k)

    const arr = changed.split('0').filter((n) => n !== '');
    console.log(arr)
    
    let answer = 0;
    for (let num of arr) {
        num = Number(num);
        if (isPrime(num)) {
            console.log(num)
            answer++;
        }
    }
    return answer
}

function isPrime(num) {
    if (num <= 1) return false;
    if (num === 2) return true;
    
    for (let i = 2; i < Math.sqrt(num) + 1; i++) {
        if (num % i === 0) return false; 
    }
    return true;
}