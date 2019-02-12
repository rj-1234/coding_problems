"""
4. Median of Two Sorted Arrays

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

"""

"""
Explanation
This is a classical coding interview question. Hard and worth thinking.

We can convert the problem to the problem of finding kth element after merging Array A and B, where k is (Array A’s length + Array B’ Length) / 2.

If any of the two arrays is empty, then the kth element is the non-empty array’s kth element.
If k == 1, the kth element is the first element of A or B.
For all other cases, we compare the (k / 2) th number in A and the (k / 2) th number in B. 
If the array has no more than k /2 elements, we set key = MAX_VALUE. 
If keyA < keyB, we get rid of first k /2 elements. 
We keep searching in the remainder for the (k – k /2) th element.
"""

# http://www.goodtecher.com/leetcode-4-median-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total = len(nums1) + len(nums2)
        if total % 2 == 1:
            return self.findkth(nums1, 0, nums2, 0, total/2 + 1)
        else:
            return (self.findkth(nums1, 0, num2, 0, total / 2) + findkth(nums1, 0, nums2, 0, total /2 + 1))/2.0
        
        
    def findkth(self, nums1, start1, nums2, start2, k):
        if (start1 >= len(nums1)):
            return nums2[start2 + k - 1]
        if (start2 >= len(nums2)):
            return nums1[start1 + k - 1]
        if k == 1:
            return min(nums1[start1], nums2[start2])
        
        index1 = start1 + k / 2 - 1
        index2 = start2 + k / 2 - 1
        key1 = nums1[int(index1)] if index1 < len(nums1) else sys.maxsize
        key2 = nums2[int(index2)] if index2 < len(nums2) else sys.maxsize
        
        if (key1 < key2):
            return self.findkth(nums1, start1 + k/2, nums2, start2, k - k /2)
        else:
            return self.findkth(nums1, start1, nums2, start2 + k/2, k - k /2)

        