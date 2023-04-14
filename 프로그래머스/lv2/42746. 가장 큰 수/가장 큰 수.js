function solution(numbers) {
    // nunber.toString() , String(number), '' + number
    numbers.sort((a, b) => {
        const number1 = Number(String(a) + String(b));
        const number2 = Number(String(b) + String(a));
        if (number1 > number2) return -1
        else if (number2 > number1) return 1
        else return 0
    })
    if (Number(numbers.join('')) === 0) return "0"
    return numbers.join('')
}