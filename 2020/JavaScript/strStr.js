var strStr = function(haystack, needle) {
    if (!haystack.includes(needle)) {
        return -1
    } else if (needle === "") {
        return 0
    } else {
        for (let i=0; i<haystack.length; i++) {
            let subString = "";
            for (let j=i; j<needle.length+i; j++) {
                subString += haystack[j];
                if (subString === needle) {
                    return i
                }
            }
        }
    }
};

console.log(strStr('hello', 'll'));
console.log(strStr('hello', 'test'));