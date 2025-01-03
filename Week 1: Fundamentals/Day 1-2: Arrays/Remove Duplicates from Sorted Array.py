"""
  Assuming nums = [0,0,1,1,1,2,2,3,3,4]
  The problem states that we should remove the duplicates such that the result remaining in non-descending order.
  For that we will need to use two pointers, one to iterate through to check 
  our values and one to serve as a place holder to modify our values.
  Left is starting as one because, the first element is automatically a unique value
"""


def removeDuplicates(nums):
    left = 1
    for right in range(1, len(nums)):
        if nums[right] != nums[right - 1]:
            nums[left] = nums[right]
            left += 1
    return left


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(removeDuplicates(nums))
