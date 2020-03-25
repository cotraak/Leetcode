# Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
#
# Example:
#
# Given array nums = [-1, 2, 1, -4], and target = 1.
#
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

def 3sumclosest(self, nums: List[int], target: int) -> int:
        s = sorted(nums)
        diff = float('inf')
        for k in range(len(nums)):
            temp = target-s[k]
            i,j = k+1, len(s)-1
            while (i<j):
                sum = s[i]+s[j]
                if sum<temp:
                    i+=1
                elif sum>temp:
                    j-=1
                else:
                    i+=1
                    j-=1
                ind = diff
                diff = min(abs(sum-temp),diff)
                if diff != ind:
                    res = sum+s[k]
        return res
