function solution(s) {
  let stack = []
  let flag = true

  const arr = Array.from(s)
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === '(') stack.push(arr[i])
    else {
      if (stack[stack.length - 1] === '(') {
        stack.pop()
      } else {
        flag = false
        break
      }
    }
  }
  if (stack.length) flag = false
  if (flag) return true
  return false
}