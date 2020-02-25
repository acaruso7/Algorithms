var deleteDuplicates = function(head) {
    for (let i=0; i<head.length; i++) {
        if (head[i]==head[i+1]) {
            head.splice(i+1, 1)
            i = 0
        } else {
            continue
        }
    }
    return head
}

console.log(deleteDuplicates([1,2,2,3,4,4,4,5]))
console.log(deleteDuplicates([1,1,2]))