function solution(s) {
  let stack = [];
  for (let i = 0; i < s.length; i++) {
    if (!stack.length) stack.push(s[i]);
    else if (s[i] === stack[stack.length - 1]) {
      stack.pop();
    } else {
      stack.push(s[i]);
    }
  }

  if (stack.length) return 0;
  else return 1;
}