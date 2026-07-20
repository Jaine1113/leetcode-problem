from collections import Counter

class Solution:
    def findAnagrams(self, s, p):
        res = []
        m = len(p)

        if len(s) < m:
            return res

        p_count = Counter(p)
        window = Counter(s[:m])

        if window == p_count:
            res.append(0)

        for i in range(m, len(s)):
            window[s[i]] += 1
            window[s[i - m]] -= 1

            if window[s[i - m]] == 0:
                del window[s[i - m]]

            if window == p_count:
                res.append(i - m + 1)

        return res