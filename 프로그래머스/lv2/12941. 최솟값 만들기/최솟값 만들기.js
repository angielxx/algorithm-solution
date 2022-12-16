function solution(A, B) {
  A.sort((a, b) => a - b)
  B.sort((a, b) => b - a)
  A = A.map((val, idx) => {
    return val * B[idx]
  })
  return A.reduce((a, b) => a + b)
}