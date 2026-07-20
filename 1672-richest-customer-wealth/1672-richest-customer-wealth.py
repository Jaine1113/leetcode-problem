class Solution:
    def maximumWealth(self, accounts):
        maxi = 0

        for i in accounts:
            total = sum(i)
            if total > maxi:
                maxi = total

        return maxi
        