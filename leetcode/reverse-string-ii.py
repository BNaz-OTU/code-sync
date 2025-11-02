class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        list_s = list(s)

        for idx in range(0, len(s), k * 2):
            left = idx
            right = idx + k - 1

            if (right > len(s) - 1):
                right = len(s) - 1

            while (left < right):
                list_s[left], list_s[right] = list_s[right], list_s[left]
                left += 1
                right -= 1
            
        return "".join(list_s)