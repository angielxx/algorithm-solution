function solution(strings, n) {
    strings.sort((a, b) => {
    if (a[n] === b[n]) {
        if (a > b) return 1
        else if (a < b) return -1
    } else {
      return a.charCodeAt(n) - b.charCodeAt(n)
    }
  })
  return strings
}