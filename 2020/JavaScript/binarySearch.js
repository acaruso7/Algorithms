var binarySearch = function(sortedList, target) {
    let left = 0;
    let right = sortedList.length - 1;
    while (left <= right) {
        let idx_mid = Math.floor((left + right)/2)
        if (sortedList[idx_mid]>target) {
            right = idx_mid - 1
        } else if (sortedList[idx_mid]<target) {
            left = idx_mid + 1
        } else {
            return idx_mid
        }
    }
    return -1
}
