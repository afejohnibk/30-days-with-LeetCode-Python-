def rob(nums):
    # If there is no house to rob
    if not nums:
        return 0
    # If it is only one house
    if len(nums) == 1:
        return nums[0]

    prev2 = 0  # dp[i-2], initially 0 since no houses robbed
    prev1 = 0  # dp[i-1], initially 0 since no houses robbed

    for num in nums:
        current = max(prev1, prev2 + num)

        prev2 = prev1
        prev1 = current

    return prev1


nums = [1, 2, 3, 1]
print(rob(nums))
