function solution(n, s) {
  // 시작 최댓값
  const share = (s / n) >> 0;

  // 베분할 수 없는 경우 (나머지를 쪼개 share에 배분해줄 값이 없다)
  if (!share) return [-1];

  // 나머지
  const rest = s % n;

  const answer = new Array(n).fill(share);
  for (let i = 0; i < rest; i++) {
    answer[answer.length - 1 - i]++;
  }
  return answer;
}
