function solution(land) {

    const arr = Array.from({ length:land.length }, (v, i) =>
                           Array.from({ length: land[0].length}, (v, j) => land[i][j]))

    for (let i = 0; i < land.length; i++) {
        if (i === 0) continue;
        for (let j = 0; j < land[0].length; j++) {
            arr[i][j] = Math.max(...arr[i - 1].filter((val, idx) => idx !== j)) + land[i][j]
        }
    }
    return Math.max(...arr[arr.length - 1])
}