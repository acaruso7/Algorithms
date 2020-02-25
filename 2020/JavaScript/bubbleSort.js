var bubbleSort = function(nums) {
    let sorted = false;
    while (!sorted) {
        let count_swapped = 0;
        for (let i=0; i<nums.length; i++) {
            if (nums[i]>nums[i+1]) {
                let temp = nums[i];
                nums[i] = nums[i+1];
                nums[i+1] = temp;
                count_swapped += 1;
            }
            if (i == nums.length-1 && count_swapped == 0) {
                sorted = true
            }
        }
    }
    return nums
}

console.log(bubbleSort([3,1,5,5,-10,1,2,3,2,3,0]))