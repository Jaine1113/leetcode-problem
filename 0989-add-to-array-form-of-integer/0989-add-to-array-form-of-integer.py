class Solution:
    def addToArrayForm(self, num, k):
        n = 0

        for i in num:
            n = n * 10 + i

        n = n + k

        ans = []

        if n == 0:
            return [0]

        while n > 0:
            ans.append(n % 10)
            n //= 10

        ans.reverse()
        return ans
        