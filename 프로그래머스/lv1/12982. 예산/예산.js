function solution(d, budget) {
  d.sort((a, b) => a - b)
  let total = 0
  let i = 0
  let flag = true
  while (i < d.length && total < budget) {
    total += d[i]
    i++
    if (total > budget) flag = false
  }
  if (flag) return i
  else return i - 1
}