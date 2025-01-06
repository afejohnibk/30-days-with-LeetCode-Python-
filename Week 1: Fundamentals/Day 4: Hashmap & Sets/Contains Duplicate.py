nums = [1, 2, 3, 4, 5]
# nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]


def containsDuplicate(nums):
    sett = set()
    for num in nums:
        if num in sett:
            return True
        sett.add(num)
    return False


print(containsDuplicate(nums))
