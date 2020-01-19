# Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
#
# Note:
#
# The solution set must not contain duplicate quadruplets.
#
# Example:
#
# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
#
# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]
# O(n^3)
def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        s = sorted(nums)
        output = set()
        if len(s)<4:
            return []
        if len(s) == 4 and sum(s) == target:
            return [s]
        for i in range(0,len(s)-1):
            temp = target - s[i]
            for j in range(i+1,len(s)):
                ind = temp - s[j]
                k,l = j+1,len(s)-1
                while k<l:
                    sm = s[k] + s[l]
                    if sm<ind:
                        k+=1
                    elif sm>ind:
                        l-=1
                    else:
                        output.add((s[k],s[l],s[j],s[i]))
                        k+=1
                        l-=1
        return list(output)
