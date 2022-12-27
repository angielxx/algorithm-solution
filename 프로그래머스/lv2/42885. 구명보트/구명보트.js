function solution(people, limit) {
  people.sort((a, b) => b - a);

  let cnt = 0;
  let l = 0;
  let r = people.length - 1;

  while (l <= r) {
    if (l === r) {
      cnt++;
      break;
    }
    if (people[l] + people[r] > limit) {
      l++;
    } else {
      l++;
      r--;
    }
    cnt++;
  }
  return cnt;
}