"""
Assuming nums = [2, 7, 11, 15], target = 9
Using two pointers l and r, we put a pointer at both ends to check if their sum == target
If not we increment the left if the sum of the two numbers is less than the target
We increment the right with -1 if the sum is greater than the target.
"""
def twoSumII(nums, target):
    l, r = 0, len(nums) - 1
    while r > l:
        if nums[l] + nums[r] == target:
            return [l+1, r+1]
        elif nums[l] + nums[r] > target:
            r -= 1
        else:
            l += 1
    return [-1, -1]


# nums = [-1, 0], target = -1
# nums = [2, 3, 4], target = 6
nums = [2, 7, 11, 15]
target = 9
print(twoSumII(nums, target))

