function solution(priorities, location) {
  let location_arr = Array.from({ length: priorities.length }, (v, k) => k++);

  // 인쇄 순서 (가장 큰 값이 맨 앞에 있을 때만 ++)
  let cnt = 0;
  while (true) {
    const MAX = Math.max(...priorities);
    const now_val = priorities.shift();
    const now_loc = location_arr.shift();
    // 가장 큰 값이면 인쇄하기(shift)
    if (now_val === MAX) {
      cnt++;
      if (now_loc === location) break;
    } else {
      priorities.push(now_val);
      location_arr.push(now_loc);
    }
  }
  return cnt;
}