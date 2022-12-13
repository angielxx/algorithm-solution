function solution(strings, n) {
  strings.sort((a, b) => {
    const gap = a.charCodeAt(n) - b.charCodeAt(n)
    if (gap === 0) {
      if (a > b) return 1
      else if (a < b) return -1
    } else {
      return gap
    }
  })
  return strings
}