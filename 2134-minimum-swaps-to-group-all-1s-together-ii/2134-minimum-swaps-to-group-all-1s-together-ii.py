class Solution:
    def minSwaps(self, nums):
        ones = sum(nums)

        if ones <= 1:
            return 0

        arr = nums + nums

        count = 0
        for i in range(ones):
            count += arr[i]

        maximum = count

        for i in range(ones, len(arr)):
            count += arr[i]
            count -= arr[i - ones]
            maximum = max(maximum, count)

        return ones - maximum
        