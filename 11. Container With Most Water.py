"""
11. Container With Most Water

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
"""

"""
ALGo -First check for the farthest distance apart and then start cinverging to the middle and keep updating the maxarea accordingly.
"""

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # maxvol = 0
        # for i in range(len(height)):
        #     for j in range(1, len(height)):
        #         vol = (j - i)*min(height[i], height[j])
        #         if vol > maxvol:
        #             maxvol = vol
        # return maxvol
        
        i = 0
        j = len(height) - 1
        maxarea = 0
        while i < j:
            if height[i] < height[j]:
                area = height[i]*(j - i)
                if area > maxarea:
                    maxarea = area
                i += 1
                
            else:
                area = height[j]*(j - i)
                if area > maxarea:
                    maxarea = area
                j -= 1
        return maxarea