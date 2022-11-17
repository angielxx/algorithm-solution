function solution(s) {
    const mid = Math.floor(s.length / 2)
    if (s.length % 2) return s[mid]
    else return s.substring(mid - 1, mid+1)
}