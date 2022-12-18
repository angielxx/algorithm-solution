function solution(n) {
  const cnt = Array.from(n.toString(2))
    .map(Number)
    .filter((x) => x === 1).length

  let i = n + 1
  while (true) {
    if (
      cnt ===
      Array.from(i.toString(2))
        .map(Number)
        .filter((x) => x === 1).length
    )
      break
    else i++
  }
  return i
}