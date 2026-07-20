class Solution:
    def maxVowels(self, s, k):
        vowels = "aeiou"

        # Count vowels in the first window
        count = 0
        for i in range(k):
            if s[i] in vowels:
                count += 1

        maximum = count

        # Slide the window
        for i in range(k, len(s)):
            # Remove left character
            if s[i - k] in vowels:
                count -= 1

            # Add right character
            if s[i] in vowels:
                count += 1

            maximum = max(maximum, count)

        return maximum
        