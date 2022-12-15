function solution(N, stages) {
  let counter = Array.from({ length: N + 2 }, (_) => 0)
  let rate = {}

  for (let i = 0; i < stages.length; i++) {
    counter[stages[i]]++
  }
  for (let stage = 1; stage <= N; stage++) {
    fail = counter[stage] / counter.slice(stage).reduce((a, b) => a + b)
    rate[stage] = fail
  }
  let answer = Object.keys(rate)
    .map(Number)
    .sort((a, b) => (rate[a] === rate[b] ? a - b : rate[b] - rate[a]))
return answer
}
