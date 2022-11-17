function solution(numbers) {
    const main = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    let answer = 0;
    for (let num of main) {
        if (!numbers.includes(num)) answer += num
    }
    return answer
}