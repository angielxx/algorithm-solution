function solution(a, b) {
    const day = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    const month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    const total = a === 1 ? b : month.slice(0, a-1).reduce((a, b) => a + b) + b
    return day[total % 7]
}
