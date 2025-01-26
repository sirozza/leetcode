
def removeElement(nums, val):
    index = 0
    for i in nums:
        if i != val:
            nums[index] = i
            index += 1
    return index, nums

print(removeElement([3,2,2,3], 3))