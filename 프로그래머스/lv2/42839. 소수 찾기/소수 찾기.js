function solution(numbers) {
    const max = 9999999;
    
    let cnt = [];
    const arr = numbers.split('').map(Number)

    // 소수 판별
    function isPrime(num) {
        if (num === 0 || num === 1) return false;
        if (num === 2) return true;
        
        for (let i = 2; i < Math.ceil(Math.sqrt(num) + 1); i++){
            if (num % i === 0) return false;
        }
        return true;
    }

    // now는 문자열
    function dfs(now, visited) {
        const num = Number(now);
        if (isPrime(num) && !cnt.includes(num)) cnt.push(num)
        
        for (let i = 0; i < arr.length; i++) {
            if (!visited.includes(i)) dfs(now + String(arr[i]), [...visited, i])
        }
    }
    
    for (let i = 0; i < arr.length; i++) {
        dfs(String(arr[i]), [i])
    }
    console.log(cnt)
    return cnt.length
}