/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    for (let i = 0; i < nums.length; i++) {
        const arr = [...nums]
        arr.splice(i, 1);
        const diff = target - nums[i];
        if (arr.includes(diff)) {
            const idx = (function () {
                for (let j = 0; j < nums.length; j++) {
                    if ((nums[j] === diff) && (j != i)) {
                        return j;
                    }
                }
            })();
            return [i, idx]
        }
    }
};