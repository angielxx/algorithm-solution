function solution(n, words) {
  // idx / n + 1 = 차례
  // idx % n + 1 = n번째 사람
  for (var i = 1; i < words.length; i++) {
    const prevWord = words[i - 1];
    const currWord = words[i];
    if (prevWord[prevWord.length - 1] !== currWord[0]) {
      break;
    }
    if (words.slice(0, i).includes(currWord)) break;
    if (i === words.length - 1) return [0, 0];
  }
  return [(i % n) + 1, Math.floor(i / n) + 1];
}