"""_summary_
    Assuming our nums = [2, 4, 12, 15, 9, 6] and target is 18
    We create a dictionary to parse in the values and their respective index, to serve as our database to store them
    Then we create a loop to interate through the values in the list, and the index, hence we will use enumerate fuction
    After which we try to get the values by first subtracting the velues with the target to get the second number
    i.e. value = target - num
    then we check if the value exists in our dictionary
    Then we assign the index to their respective values and return the index of the two numbers added together to give the target
"""


def twoSum(nums, target):
    ddict = {}
    for index, num in enumerate(nums):
        value = target - num
        if value in ddict:
            return [ddict[value], index]
        ddict[num] = index
    return []


nums = [2, 4, 12, 15, 9, 6]
target = 18
print(twoSum(nums, target))

