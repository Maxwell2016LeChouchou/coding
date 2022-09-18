# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

 

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

def maxSubArray(nums):
    max_sums = nums[0]
    for i in range(1, len(nums)):
        nums[i] = max(nums[i]+nums[i-1], nums[i])
        if nums[i] > max_sums:
            max_sums = nums[i]

    return max_sums

nums =  [50,-10,-3,4,-1,2,1,-5,4]

print(maxSubArray(nums))
