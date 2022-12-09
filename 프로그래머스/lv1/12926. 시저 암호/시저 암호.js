function solution(s, n) {
  let arr = Array.from(s)
  arr = arr.map((char) => {
    return char.charCodeAt()
  })
  arr = arr.map((code) => {
    // 대문자인 경우
    if (code >= 65 && code <= 90) {
      code += n
      if (code > 90) code = 64 + (code - 90)
    }
    // 소문자인 경우
    else if (code >= 97 && code <= 122) {
      code += n
      if (code > 122) code = 96 + (code - 122)
    }
    return code
  })
  return String.fromCharCode(...arr)
}