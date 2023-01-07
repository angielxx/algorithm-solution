function solution(name) {
  let answer = 0;

  min_move = name.length - 1;
  for (let i = 0; i < name.length; i++) {
    // console.log(name[i]);
    // console.log(name[i].charCodeAt() - 'A'.charCodeAt());
    // console.log('Z'.charCodeAt() - name[i].charCodeAt() + 1);
    answer += Math.min(
      name[i].charCodeAt() - 'A'.charCodeAt(),
      'Z'.charCodeAt() - name[i].charCodeAt() + 1
    );
    // console.log(answer);

    next = i + 1;
    while (next < name.length && name[next] == 'A') {
      next += 1;
    }
    min_move = Math.min(
      min_move,
      2 * i + name.length - next,
      i + 2 * (name.length - next)
    );
  }
  // console.log(min_move);
  answer += min_move;
  return answer;
}

