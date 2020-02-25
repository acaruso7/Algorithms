var reverseInt = function(x) {
    let str = x.toString();
    if (str[0]=="-") {
        str = str.slice(1)
        var negative = true
    }
    let reversedStr = "";
    for (let i = str.length-1; i>=0; i--) {
        reversedStr += str[i];
    }
    let reversedInt = parseInt(reversedStr)
    if (negative) {
        reversedInt *= -1
    }
    return reversedInt
}

console.log(reverseInt(-123))