def subsets(nums):
    result = []

    def backtrack(start, current):
        result.append(current[:])

        for i in range(start, len(nums)):
            # includes nums[i]
            current.append(nums[i])
            backtrack(i + 1, current)
            # excludes nums[i]
            current.pop()

    backtrack(0, [])
    return result


nums = [1, 2, 3]
print(subsets(nums))

