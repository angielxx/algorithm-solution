function solution(arr) {
    let min = Infinity
    let min_idx = 0;
    for (let i in arr) {
        const val = arr[i]
        if (val < min) {
            min = val
            min_idx = i
        }
    }
    arr.splice(min_idx, 1)
    if (!arr.length) return [-1];
    return arr
}