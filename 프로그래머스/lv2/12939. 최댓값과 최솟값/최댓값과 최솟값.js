function solution(s) {
    let answer = '';
    let nums = s.split(' ').map(x => {return Number(x)})
    let max = Math.max(...nums)
    let min = Math.min(...nums)
    answer = `${min} ${max}`
    return answer;
}