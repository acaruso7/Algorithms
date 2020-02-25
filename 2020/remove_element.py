# Given an array nums and a value val, remove all instances of that value in-place and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.

# EXAMPLE:
# Given nums = [3,2,2,3], val = 3,
# Your function should return length = 2, with the first two elements of nums being 2.

def removeElement(nums: list, val: int) -> int:
    if nums == []:
        return(0)
    elif len(nums) == 1 and nums[0] == val:
        return(0)
    while nums[0] == val:
        nums.remove(val)
        if len(nums) == 1 and nums[0] == val:
            return(0)

    idx = 0
    while idx < len(nums):
        if nums[idx] == val:
            nums.remove(nums[idx])
            idx -= 1
        else:
            idx += 1
    return(len(nums))

print(removeElement([3,2,2,3], 3))
print(removeElement([0,1,2,2,3,0,4,2], 2))
print(removeElement([1], 1))
print(removeElement([3,3], 3))