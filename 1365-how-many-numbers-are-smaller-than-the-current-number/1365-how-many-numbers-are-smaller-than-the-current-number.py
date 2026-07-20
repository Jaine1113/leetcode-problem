class Solution:
    def smallerNumbersThanCurrent(self, nums):
        sorted_nums = sorted(nums)
        pos = {}

        for i, num in enumerate(sorted_nums):
            if num not in pos:
                pos[num] = i

        return [pos[num] for num in nums]  