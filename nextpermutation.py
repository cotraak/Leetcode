# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
#
# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
#
# The replacement must be in-place and use only constant extra memory.
#
# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
#
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
#

def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = len(nums) - 1
        m= float('inf')
        t = m
        count = 0
        if len(nums) == 1:
            nums = nums
        else:
            while nums[j-1]>=nums[j] and j>=1:
                j-=1
            k = j-1
            if k<0:
                nums.reverse()
            else:
                for i in range(k+1,len(nums)):
                    if nums[i] > nums[k]:
                        m = min(m,nums[i] - nums[k])
                        if m == nums[i]-nums[k]:
                            s = nums[i]
                            r = i
                        t = m
                        count+=1
                if count == 0:
                    nums.reverse()
                else:
                    temp = s
                    nums[r] = nums[k]
                    nums[j-1] = temp
                    nums[k+1:] = nums[k+1:][::-1]
