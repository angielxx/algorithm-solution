function solution(nums) {
  function isPrimeNum(num) {
    for (let i = 2; i <= Math.ceil(Math.sqrt(num)); i++) {
      if (num % i === 0) return false
    }
    return true
  }
  let cnt = 0
  for (let i = 0; i < nums.length - 2; i++) {
    for (let j = i + 1; j < nums.length - 1; j++) {
      for (let k = j + 1; k < nums.length; k++) {
        total = nums[i] + nums[j] + nums[k]
        if (isPrimeNum(total)) cnt++
      }
    }
  }
  return cnt
}