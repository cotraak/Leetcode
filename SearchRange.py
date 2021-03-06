# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
#
# Example 1:
#
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:
#
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

def SearchRange(nums, target):
        if len(nums) == 0:
            return [-1,-1]
        for i in range(0,len(nums)):
            if nums[i] == target:
                break
        if i == len(nums) -1 and nums[i] != target:
            return [-1,-1]
        start = i
        while nums[i] == target:
            if i == len(nums)-1:
                i+=1
                break
            else:
                i+=1
        end = i-1
        return [start,end]
