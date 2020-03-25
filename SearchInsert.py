# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
#
# You may assume no duplicates in the array.
#
# Example 1:
#
# Input: [1,3,5,6], 5
# Output: 2
# Example 2:
#
# Input: [1,3,5,6], 2
# Output: 1
# Example 3:
#
# Input: [1,3,5,6], 7
# Output: 4
# Example 4:
#
# Input: [1,3,5,6], 0
# Output: 0

def SearchInsert(nums, target):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            if target==nums[0] or nums[0]>target:
                return 0
            elif nums[0]<target:
                return 1
        if nums[0]>target:
            return 0
        for i in range(0,len(nums)):
            if nums[i] == target:
                return i
            elif nums[i]<target:
                res = i
        return res+1
