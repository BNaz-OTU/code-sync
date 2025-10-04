class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        tempString = ""

        for val in s:
            tempString += val
            size = len(s) / len(tempString)

            if (size == 1):
                return False

            if ((tempString * int(size)) == s):
                return True