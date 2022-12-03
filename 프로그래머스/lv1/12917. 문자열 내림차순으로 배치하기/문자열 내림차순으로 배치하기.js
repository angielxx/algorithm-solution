function solution(s) {
    const arr = Array.from(s);
    arr.sort((a, b) => {
        return b.charCodeAt() - a.charCodeAt()
    })
    return arr.join('')
}