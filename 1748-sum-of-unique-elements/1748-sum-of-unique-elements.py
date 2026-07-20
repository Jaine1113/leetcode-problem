from collections import Counter

class Solution:
    def sumOfUnique(self, nums):
        count = Counter(nums)
        s = 0

        for num in count:
            if count[num] == 1:
                s += num

        return s
        