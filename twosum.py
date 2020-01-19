# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

def twoSum(self, nums, target):
        d1 = dict()
        d2 = dict()
        for i in range(0,len(nums)):
            temp = nums[i]
            d1[temp] = i
        for j in range(0,len(nums)):
            temp1 = target - nums[j]
            if (temp1 in list(d1.keys()) and d1.get(temp1) !=j):
                return [j,d1.get(temp1)]
