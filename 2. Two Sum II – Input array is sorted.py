"""
2. Two Sum II – Input array is sorted
Question:
Similar to Question [1. Two Sum], except that the input array is already sorted in
ascending order.
"""

class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(numbers) - 1
        for x in range(len(numbers)):
            if numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] < target:
                i += 1
            elif numbers[i] + numbers[j] == target:
                return [i+1, j+1]