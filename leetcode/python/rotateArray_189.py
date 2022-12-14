# Given an array, rotate the array to the right by k steps, where k is non-negative.

# Follow up:

# Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
# Could you do it in-place with O(1) extra space?
 

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

def rotate(nums, k):
    new_nums = []
    for i in range(len(nums)-k, len(nums)):
        new_nums.append(nums[i])
    for j in range(len(nums)-k):
        new_nums.append(nums[j])
    for p in range(len(nums)):
        nums[p] = new_nums[p]
    print(nums)

nums = [1,2,3,4,5,6,7]
k = 2
rotate(nums, k)

    

