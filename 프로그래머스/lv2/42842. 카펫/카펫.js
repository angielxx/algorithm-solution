function solution(brown, yellow) {
  if (yellow === 1) return [3, 3]
  let height
  let width
  
  // 약수 찾기
  for (let i = 2; i <= Math.ceil(Math.sqrt(yellow)); i++) {
    if (yellow % i === 0) {
      area = (yellow / i + 2) * (i + 2)
      if (area === brown + yellow) {
        height = i + 2 > yellow / i + 2 ? yellow / i + 2 : i + 2
        width = i + 2 > yellow / i + 2 ? i + 2 : yellow / i + 2
        break
      }
    }
  }
  return [width, height]
}