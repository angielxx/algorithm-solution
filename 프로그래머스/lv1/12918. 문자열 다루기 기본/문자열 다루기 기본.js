function solution(s) {
    const arr = Array.from(s);
    if (![4,6].includes(arr.length)) return false;
    for (let item of arr) {
        if(isNaN(item)) return false
    }
    return true
}