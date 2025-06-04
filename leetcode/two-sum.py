class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen_nums = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen_nums:
                return [seen_nums[diff], i]
            seen_nums[num] = i