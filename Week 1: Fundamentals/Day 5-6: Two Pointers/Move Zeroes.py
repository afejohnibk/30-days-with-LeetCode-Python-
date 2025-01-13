"""
Been a while I wrote anything in comment
Well this was one interesting topic for messagesmoving the zeros while stil in-place
Using two pointers left and right to swap the numbers and still maintain the order of the non-zero numbers
"""


def moveZeroes(nums):
    l = 0
    for r in range(len(nums)):
        if nums[r] != 0:
            nums[r], nums[l] = nums[l], nums[r]
            l += 1
    return nums


nums = [0, 1, 0, 3, 12]
print(moveZeroes(nums))
