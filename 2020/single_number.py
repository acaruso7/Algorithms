# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
# should have linear runtime complexity

#EXAMPLE:
# Input: [4,1,2,1,2]
# Output: 4

def singleNumber(nums:list) -> int:
    counts = {nums.count(x):x for x in nums}
    return(counts[1])

print(singleNumber([4,1,2,1,2]))


    
