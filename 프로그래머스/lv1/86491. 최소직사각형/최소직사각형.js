function solution(sizes) {
    let width = []
    let height = []
    for (let i = 0; i < sizes.length; i++) {
        const a = sizes[i][0]
        const b = sizes[i][1]
        if (a > b) {
            width.push(a)
            height.push(b)
        } else {
            width.push(b)
            height.push(a)
        }
    }
    return Math.max(...width) * Math.max(...height)
}