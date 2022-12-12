function solution(n, arr1, arr2) {
  arr1 = arr1.map((el, i) =>
    (el | arr2[i])
      .toString(2)
      .padStart(n, 0)
      .replace(/0/g, ' ')
      .replace(/1/g, '#'),
  )
  return arr1
}