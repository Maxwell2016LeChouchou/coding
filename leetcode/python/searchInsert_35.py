# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You may assume no duplicates in the array.

# Example 1:

# Input: [1,3,5,6], 5
# Output: 2
# Example 2:

# Input: [1,3,5,6], 2
# Output: 1


def searchInsert(nums, target):
    if target not in nums:
        for i in range(len(nums)):
            if target<nums[i]:
                return i
        return len(nums) 
    else:
        return nums.index(target)

nums = [1, 3, 5, 6]
target = 4
print(searchInsert(nums, target))
 