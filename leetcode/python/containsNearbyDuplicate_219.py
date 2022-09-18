# Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true
# Example 2:

# Input: nums = [1,0,1,1], k = 1
# Output: true
# Example 3:

# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false


def containsNearbyDuplicate(nums, k):
    if len(nums) == len(set(nums)):
        return False

    if len(nums) <= k + 1:  # k is big enough to cover the entire list
        return True
    
    for i in range(len(nums)-k):
        if len(nums[i: (i+k+1)]) != len(set(nums[i:(i+k+1)])):
            return True
    
    return False


nums = [1,2,3,4,1]
k = 4

print(containsNearbyDuplicate(nums, k))