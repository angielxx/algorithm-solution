function solution(array, commands) {
  let answer = []
  for (let a = 0; a < commands.length; a++) {
    const [i, j, k] = commands[a]
    let part = array.slice(i - 1, j)
    part.sort((b, c) => b - c)
    answer.push(part[k - 1])
  }
  //   console.log(answer)
  return answer
}