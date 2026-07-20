class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            s = 0
            while num > 0:
                digit = num % 10
                s = s + digit
                num = num // 10
            num = s
        return num
        