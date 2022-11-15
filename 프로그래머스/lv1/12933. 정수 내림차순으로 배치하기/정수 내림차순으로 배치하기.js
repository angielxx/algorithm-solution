function solution(n) {
    let arr = Array.from(String(n))
    arr = arr.map(el => Number(el))
    arr.sort(function(a,b){
        return b-a
    })
    let answer = '';
    arr.forEach(el => answer += el)
    return Number(answer)
}