class Solution:
    def findMaxConsecutiveOnes(self, nums):
        count = 0
        maxi = 0

        for i in nums:
            if i == 1:
                count += 1
                if count > maxi:
                    maxi = count
            else:
                count = 0

        return maxi
        