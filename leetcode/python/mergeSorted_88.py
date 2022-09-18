# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

# Note:

# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
# Example:

# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3

# Output: [1,2,2,3,5,6]

def merge(nums1, nums2):

    nums3 = []
    ls1 = 0
    ls2 = 0

    for i in range(m+n):
        if ls1 == m:
            nums3 = nums3 + nums2[ls2:]
        if ls2 == n:
            nums3 = nums3 + nums1[ls1:]
        if nums1[ls1] < nums2[ls2]:
            nums3.append(nums1[ls1])
            ls1 += 1
        else: 
            nums3.append(nums2[ls2])
            ls2 += 1
        
    return nums3
