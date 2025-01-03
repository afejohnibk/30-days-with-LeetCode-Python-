"""
  Assuming nums = [-2,1,-3,4,-1,2,1,-5,4]
  Bsed on the example we need to find the subarray with the largest sum 
  i.e. [1,3,5,4,-1,-5,1] the subarray will be [1,3,5,4] which it's sum will give 13, any other subarray will be less than 13
"""


def maxSubarray(nums):
    c = 0
    max_sum = 0
    for i in range(len(nums)):
        c += nums[i]
        max_sum = max(max_sum, c)
        if c < 0:
            c = 0
    return max_sum


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubarray(nums))
