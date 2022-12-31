function solution(progresses, speeds) {
  let answer = [];
  while (progresses.length) {
    for (let i = 0; i < progresses.length; i++) {
      progresses[i] += speeds[i];
    }

    cnt = 0;
    while (progresses[0] >= 100) {
      progresses.shift();
      speeds.shift();
      cnt++;
      if (!progresses.length) {
        break;
      }
    }
    if (cnt > 0) {
      answer.push(cnt);
      cnt = 0;
    }
  }
  return answer;
}