var factorial = function(n) {
    let runningProduct = 1;
    for (let i=2; i<=n; i++) {
        runningProduct *= i;
    }
    return runningProduct;
}

console.log(factorial(4)) //24


var factorialRecursive = function(n) {
    if (n==1) {
        return 1
    } else {
        return n*factorialRecursive(n-1)
    }
}

console.log(factorialRecursive(4)) //24