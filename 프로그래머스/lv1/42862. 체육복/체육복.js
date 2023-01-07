function solution(n, lost, reserve) {
  let arr = Array.from({ length: n + 2 }, (_) => 1);
  lost.forEach((x) => arr[x]--);
  reserve.forEach((x) => arr[x]++);
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] === 2 && arr[i - 1] === 0) {
      arr[i]--;
      arr[i - 1]++;
    } else if (arr[i] === 2 && arr[i + 1] === 0) {
      arr[i]--;
      arr[i + 1]++;
    }
  }
  return arr.filter((val, idx) => 0 < idx && idx <= n && val > 0).length;
}