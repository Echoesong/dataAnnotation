def create_staircase(nums):
    while len(nums) != 0:
        step = 1
        subsets = []
        if len(nums) >= step:
            subsets.append(nums[0:step])
            nums = nums[step:]
            step += 1
        else:
            return False

    return subsets


numbers = [1, 2, 3, 4, 5, 6]
print(create_staircase(numbers))
