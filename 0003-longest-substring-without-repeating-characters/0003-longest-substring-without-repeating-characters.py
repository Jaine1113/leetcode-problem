class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0

        for i in range(len(s)):
            sub = ""
            for j in range(i, len(s)):
                if s[j] in sub:
                    break
                sub += s[j]
            ans = max(ans, len(sub))

        return ans
        