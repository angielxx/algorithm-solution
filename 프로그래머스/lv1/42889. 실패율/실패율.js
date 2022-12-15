function solution(N, stages) {
  let rate = {}

  for (let stage = 1; stage <= N; stage++) {
    fail =
      stages.filter((x) => x === stage).length /
      stages.filter((x) => x >= stage).length
    rate[stage] = fail
  }

  return Object.keys(rate)
    .map(Number)
    .sort((a, b) => (rate[a] === rate[b] ? a - b : rate[b] - rate[a]))
}