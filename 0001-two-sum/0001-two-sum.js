/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    for (let i = 0; i < nums.length; i++) {
        console.log('nums', nums);
        console.log('i', i)
        const arr = [...nums]
        arr.splice(i, 1);
        const diff = target - nums[i];
        console.log('arr', arr);
        console.log('diff', diff);
        if (arr.includes(diff)) {
            console.log('i', i)
            const idx = (function () {
                for (let j = 0; j < nums.length; j++) {
                    console.log('j', j)
                    if ((nums[j] === diff) && (j != i)) {
                        console.log('j')
                        return j;
                    }
                }
            })();
            return [i, idx]
        }
    }
};