function solution(n) {
    const answer = [];
    
    function hanoi(num, from, to, other) {
        if (num === 0) return
        if (num === 1) {
            answer.push([from, to])
            return [from, to]
        }

        hanoi(num - 1, from, other, to)
        answer.push([from, to])
        hanoi(num - 1, other, to, from)
    }
    
    hanoi(n, 1, 3, 2)
    return answer
}