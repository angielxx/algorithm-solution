function solution(bridge_length, weight, truck_weights) {
  // 다리를 건너는 트럭
  let passing = [];
  // 시간
  let time = 0;

  while (truck_weights.length || passing.length) {
    // 시간경과
    time++;
    passing = passing.map((x) => {
      return [x[0], x[1] + 1];
    });

    // 다리를 건넌 트럭 필터링
    passing = passing.filter((x) => x[1] <= bridge_length);
    // console.log('here', passing);
    // 현재 다리 위의 무게
    let current_weight = 0;
    passing.forEach((x) => (current_weight += x[0]));
    // console.log();

    // 다음 차례의 트럭을 다리에 올릴 수 있는지 판단
    if (current_weight + truck_weights[0] <= weight) {
      // [무게, 경과시간]으로 저장
      passing.push([truck_weights.shift(), 1]);
    }
    // console.log(time, passing, truck_weights);
  }
  return time;
}