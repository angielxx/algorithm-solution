 function solution(answers) {
  const p1 = [1, 2, 3, 4, 5];
  const p2 = [2, 1, 2, 3, 2, 4, 2, 5];
  const p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];

  let cnt1 = 0;
  let cnt2 = 0;
  let cnt3 = 0;

  let cnt = {
    1: 0,
    2: 0,
    3: 0,
  };

  answers.forEach((val, idx) => {
    if (val === p1[idx % p1.length]) cnt[1]++;
    if (val === p2[idx % p2.length]) cnt[2]++;
    if (val === p3[idx % p3.length]) cnt[3]++;
  });
  const MAX = Math.max(...Object.values(cnt));

  return Object.keys(cnt)
    .filter((k) => cnt[k] === MAX)
    .map(Number)
    .sort((a, b) => a - b);
}