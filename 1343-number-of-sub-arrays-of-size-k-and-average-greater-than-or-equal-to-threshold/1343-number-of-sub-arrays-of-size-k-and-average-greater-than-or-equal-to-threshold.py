class Solution:
    def numOfSubarrays(self, arr, k, threshold):
        target = k * threshold
        window = sum(arr[:k])
        count = 0

        if window >= target:
            count += 1

        for i in range(k, len(arr)):
            window += arr[i] - arr[i - k]
            if window >= target:
                count += 1

        return count
        