var fib = function(n) {
    //return the nth element of the fibonacci sequence
    let nums = [1,1];
    let count = 0;
    while (count < n-1) {
        let sum = nums[0] + nums[1];
        nums[0] = nums[1];
        nums[1] = sum;
        count++;
    }
    return nums[0]
}

// 1, 1, 2, 3, 5, 8
console.log(fib(6)) //8
console.log(fib(4)) //3