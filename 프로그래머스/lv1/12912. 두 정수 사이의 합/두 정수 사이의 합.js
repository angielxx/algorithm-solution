function solution(a, b) {
    let sum = 0;
    if (a > b) {
        temp = a
        a = b
        b = temp
    }
    while (a <= b) {
        sum += a;
        a++;
    }
    return sum
}