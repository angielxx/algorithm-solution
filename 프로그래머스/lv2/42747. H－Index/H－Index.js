function solution(citations) {
  let answer = 0;
  citations.sort((a, b) => a - b);
  const n = citations.length;
  for (let i = 0; i < n; i++) {
    const hIndex = n - i;
    if (citations[i] >= hIndex) {
      answer = hIndex;
      break;
    }
  }
  return answer;
}