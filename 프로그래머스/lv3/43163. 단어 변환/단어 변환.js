function solution(begin, target, words) {
  let answer = 0;
  let visited = [];
  let queue = [];

  if (!words.includes(target)) return 0;

  // [현재단어, 변경횟수]
  queue.push([begin, 0]);

  while (queue.length) {
    let [v, cnt] = queue.shift();

    if (v === target) {
      return cnt;
    }

    for (let word of words) {
      // 방문한 경우 패스
      if (visited.includes(word)) continue;

      let notEqual = 0;
      for (let i = 0; i < word.length; i++) {
        if (word[i] !== v[i]) notEqual++;
      }
      if (notEqual === 1) {
        queue.push([word, ++cnt]);
        visited.push(word);
      }
    }
  }
  return answer;
}
