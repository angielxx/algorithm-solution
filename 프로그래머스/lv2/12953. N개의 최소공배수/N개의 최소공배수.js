function solution(arr) {
  // a > b
  function gcd(a, b) {
    while (b !== 0) {
      let r = a % b;
      a = b;
      b = r;
    }
    return a;
  }

  function lcm(a, b) {
    return (a * b) / gcd(a, b);
  }

  arr.sort((a, b) => a - b);
  return arr.reduce((a, b) => lcm(b, a));
}