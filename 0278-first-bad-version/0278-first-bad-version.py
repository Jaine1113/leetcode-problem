# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# The isBadVersion API is already provided.

class Solution:
    def firstBadVersion(self, n):
        left, right = 1, n

        while left < right:
            mid = (left + right) // 2

            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return left
        