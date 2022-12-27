function solution(n, a, b) {
  let numbers = Array.from({ length: n }, (v, i) => i + 1);
  let round = 0;
  let found = false;
  while (!found) {
    round++;
    let temp = [];
    for (let i = 0; i < numbers.length; i += 2) {
      if (
        [numbers[i], numbers[i + 1]].includes(a) &&
        [numbers[i], numbers[i + 1]].includes(b)
      ) {
        found = true;
        break;
      } else {
        if ([numbers[i], numbers[i + 1]].includes(a)) temp.push(a);
        else if ([numbers[i], numbers[i + 1]].includes(b)) temp.push(b);
        else temp.push(numbers[i]);
      }
    }
    numbers = temp;
  }
  return round;
}