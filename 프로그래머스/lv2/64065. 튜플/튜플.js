function solution(s) {
    let arr = s.slice(2, s.length - 2).split('},{');
    arr = arr.map((x) => {return x.split(',').map(Number)})
    arr.sort((a, b) => a.length - b.length)
    
    const answer = [];
    arr.forEach((x) => answer.push(...x.filter((a) => !answer.includes(a))))
    // console.log(answer)
    return answer
}