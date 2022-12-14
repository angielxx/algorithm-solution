function solution(number) {
    let cnt = 0
    for (let i = 0; i < number.length - 2; i++) {
        for (let j = i+1; j < number.length - 1; j++) {
            const sum = number[i] + number[j]
            for (let k = j+1; k < number.length; k++) {
                if (number[k] === (-1)*sum) cnt++
            }
        }
    }
    return cnt
}