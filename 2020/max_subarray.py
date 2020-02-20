def maxSubArray(nums: list) -> int:
    max_curr = nums[0]
    max_global = nums[0]
    for idx in range(1, len(nums)):
        max_curr = max(nums[idx], max_curr + nums[idx])
        if max_curr > max_global:
            max_global = max_curr
    return(max_global)
        

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) # 6