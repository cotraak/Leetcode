# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
#
# You may assume nums1 and nums2 cannot be both empty.
#
# Example 1:
#
# nums1 = [1, 3]
# nums2 = [2]
#
# The median is 2.0
# Example 2:
#
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# The median is (2 + 3)/2 = 2.5
def findMedianSortedArrays(self, nums1, nums2):
        nums = nums1 + nums2
        nums = sorted(nums)
        n = len(nums)
        if n%2 == 1:
            id1 = int((n-1)/2)
            median = float(nums[id1])
        else:
            id2 = int((n/2)-1)
            id3 = int((n/2))
            median = float((nums[id2]+nums[id3])/2)
        return median
