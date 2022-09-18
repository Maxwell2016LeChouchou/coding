# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].

def twoSum(nums, target):
    dic = {}
    for i in range(len(nums)):
        expected = target - nums[i]
        if expected in dic.keys():
            return [dic[expected], i]
        dic[nums[i]] = i

nums = [2,11,7,15]
print(twoSum(nums,9))
