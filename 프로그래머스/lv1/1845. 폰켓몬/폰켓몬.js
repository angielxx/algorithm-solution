function solution(nums) {
  const total = nums.length / 2;
  const species = {};
  for (let num of nums) {
    if (Object.keys(species).includes(String(num))) species[num]++;
    else species[num] = 1;
  }
  if (Object.keys(species).length >= total) return total;
  else return Object.keys(species).length;
}