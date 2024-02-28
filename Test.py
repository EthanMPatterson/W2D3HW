def negate(nums):
    for i in range(len(nums)):
        if nums [i] > 0:
            nums [i] = -nums[i]
    print(nums)

negate([100, 534, 32, 15, 77, 222, 788, 345, 75645, 22])