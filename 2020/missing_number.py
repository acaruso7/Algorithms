# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
# should have linear runtime complexity

# EXAMPLE:
# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8

def missingNumber(nums: list) -> int:
    all_nums = list(range(len(nums)+1))
    for x in all_nums:
        if x not in nums:
            return(x)

assert missingNumber([9,6,4,2,3,5,7,0,1]) == 8
print('test passed')